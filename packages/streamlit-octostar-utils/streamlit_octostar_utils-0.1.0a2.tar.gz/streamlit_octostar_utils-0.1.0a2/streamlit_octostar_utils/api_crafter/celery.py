from pathlib import Path
from celery import Celery, states
import subprocess
import logging
import time
import os
import shutil
import json
from functools import partial
from celery.signals import before_task_publish, task_prerun
from lib.fastapi_utils import Route, CommonModels, DefaultErrorRoute

# Be careful! There can be only one instance of this in an application
class CeleryExecutor(object):    
    AWAITING = "AWAITING"
    global_instance = None
    
    def __init__(self, name, module_name, base_folder=os.getcwd(), cleanup_every_secs=(3600, 60)):
        self.name = name
        self.base_folder = base_folder
        self.filename = module_name # os.path.splitext(os.path.basename(base_folder))[0]
        root = Path(base_folder).resolve().joinpath('data')
        self.processed_folder = root.joinpath('results')
        
        _folders = {
            'data_folder_in': root.joinpath('in'),
            'data_folder_out': root.joinpath('in'),
        }

        for folder in list(_folders.values()) + [self.processed_folder]:
            shutil.rmtree(folder, ignore_errors=True)
            os.makedirs(folder, exist_ok=True)
        self.app = Celery(self.filename)
        self.app.conf.result_backend = 'file://{}'.format(str(self.processed_folder))
        self.app.conf.broker_url = 'filesystem://localhost:6379'
        self.app.conf.broker_transport_options = {k: str(f) for k, f in _folders.items()}
        self.app.conf.task_serializer = 'json'
        self.app.conf.persist_results = True
        self.app.conf.result_serializer = 'pickle'
        self.app.conf.accept_content = ['application/json', 'application/x-python-serialize']
        self.app.conf.result_expires=cleanup_every_secs[0]
        self.app.conf.cleanup_every=cleanup_every_secs[1]
        self.set_cleanup_task()
        CeleryExecutor.global_instance = self
        self.inject_task_statuses()
        self.process = None

    def set_cleanup_task(self):
        def cleanup_filesystem_backend(result_dir=None, max_age=3600):
            now = time.time()
            if not result_dir:
                return
            for filename in os.listdir(result_dir):
                file_path = os.path.join(result_dir, filename)
                if os.path.isfile(file_path) and now - os.path.getmtime(file_path) > max_age:
                    os.remove(file_path)
                    logging.warning(f"Deleted {file_path}")
        self.app.task(cleanup_filesystem_backend)
        self.app.conf.beat_schedule = {
            'cleanup-filesystem-backend': {
                'task': f'{self.__class__.__module__}.cleanup_filesystem_backend',
                'schedule': self.app.conf.cleanup_every,
                'args': (self.processed_folder, self.app.conf.result_expires)
            },
        }

    def start(self):
        self.process = subprocess.Popen(['celery', f'--app={self.filename}.{self.name}', 'worker', '--loglevel=info', '-B'])

    def close(self):
        self.process.kill()

    @staticmethod
    def _set_global_task_awaiting(headers=None, **kwargs):
        task_id = headers['id']
        result = CeleryExecutor.global_instance.app.AsyncResult(task_id)
        result.backend.store_result(task_id, None, state=CeleryExecutor.AWAITING)

    @staticmethod
    def _set_global_task_started(task_id=None, **kwargs):
        result = CeleryExecutor.global_instance.app.AsyncResult(task_id)
        result.backend.store_result(task_id, None, state=states.STARTED)

    def inject_task_statuses(executor):
        before_task_publish.connect(CeleryExecutor._set_global_task_awaiting)
        task_prerun.connect(CeleryExecutor._set_global_task_started)

class FastAPICeleryTaskRoute(Route):
    def __init__(self, app, celery_app, router=None):
        super().__init__(app, router)
        self.celery_app = celery_app
        self.define_routes()
    
    def define_routes(self):
        @Route.route(self, path="/task/{task_id}", methods=["DELETE"], summary='Cancel a queued or running task.',
            status_code=200, responses=DefaultErrorRoute.error_responses)
        async def delete_task(
            task_id: str
        ) -> CommonModels.OKResponseModel:
            self.celery_app.control.revoke(task_id, terminate=True)
            return CommonModels.OKResponseModel()

        @Route.route(self, path="/task/{task_id}", methods=["GET"], summary='Get task status (and result if available).',
            status_code=200, responses=DefaultErrorRoute.error_responses)
        async def get_task(
            task_id: str
        ) -> CommonModels.DataResponseModel:
            task = self.celery_app.AsyncResult(task_id)
            data = {}
            status = "success"
            if task.state == "FAILURE":
                error_response = DefaultErrorRoute.format_error(task.result).body.decode('utf-8')
                data = {"task_state": task.state, "task_id": task_id, "data": json.loads(error_response)}
            elif task.state == "PENDING":
                data = {"task_state": "UNKNOWN", "task_id": task_id}
            elif task.state in ["AWAITING", "STARTED"]:
                data = {"task_state": task.state, "task_id": task_id}
            elif task.state == "SUCCESS":
                data = {"task_state": task.state, "task_id": task_id, "data": task.result}
            elif task.state == "STARTED":
                data = {"task_status": "STARTED", "task_id": task_id}
            else:
                raise ValueError("Unknown task state!")
            return CommonModels.DataResponseModel(data=data, status=status)

def task():
    def decorator(func):
        return func
    return decorator