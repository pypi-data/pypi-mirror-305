import json
import pickle
import logging
import os
import threading
import time
from types import FunctionType
from typing import Any, Callable

import redis

from callite.rpctypes.response import Response
from callite.shared.redis_connection import RedisConnection


# import pydevd_pycharm
# pydevd_pycharm.settrace('host.docker.internal', port=4444, stdoutToServer=True, stderrToServer=True)

log_level = os.getenv('LOG_LEVEL', 'ERROR')
log_level = getattr(logging, log_level.upper(), 'ERROR')

# TODO: Check method calls and parameters
class RPCServer(RedisConnection):
    def __init__(self, conn_url: str, service: str, *args, **kwargs):
        super().__init__(conn_url, service, *args, **kwargs)
        self._registered_methods = {}
        self._xread_groupname = kwargs.get('xread_groupname', 'generic')

        t = threading.Thread(target=self._subscribe_redis, daemon=True)
        t.start()
        self._logger = logging.getLogger(__name__)
        self._logger.addHandler(logging.StreamHandler())
        self._logger.setLevel(log_level)

    def subscribe(self, handler: FunctionType | Callable, method_name: str | None = None) -> None:
        method_name = method_name or handler.__name__
        self._registered_methods[method_name] = {'func': handler, 'returns': False}
        return handler

    def register(self, handler: FunctionType | Callable, method_name: str | None = None) -> Callable:
        method_name = method_name or handler.__name__
        self._registered_methods[method_name] = {'func': handler, 'returns': True}
        return handler

    def run_forever(self) -> None:
        while self._running: time.sleep(1000000)


    def _subscribe_redis(self):
        self._create_redis_group()
        while self._running:
            messages = self._read_messages_from_redis()
            self._process_messages(messages)

    def _create_redis_group(self):
        try:
            self._rds.xgroup_create(f'{self._queue_prefix}/request/{self._service}', self._xread_groupname, mkstream=True)
        except redis.exceptions.ResponseError as e:
            if "name already exists" not in str(e): raise

    def _read_messages_from_redis(self):
        messages = self._rds.xreadgroup(self._xread_groupname, self._connection_id, {f'{self._queue_prefix}/request/{self._service}': '>'}, count=1, block=1000, noack=True)
        self._logger.info(f"{len(messages)} messages received from {self._queue_prefix}/request/{self._service}")
        return messages

    def _process_messages(self, messages):
        for _, message_list in messages:
            for _message in message_list:
                message_id, message_data = _message
                request = pickle.loads(message_data[b'data'])
                self._logger.info(f"Processing message {message_id} with data: {request}")
                self._handle_messages(request, message_id)

    def _handle_messages(self, request, message_id):
        threading.Thread(target=self._process_single, args=(request, message_id), daemon=True).start()

    def _process_single(self, request, message_id):

        self._rds.xack(f'{self._queue_prefix}/request/{self._service}', self._xread_groupname, message_id)
        if request.method not in self._registered_methods:
            raise Exception(f"Method {request.method} not registered")

        returns = self._registered_methods[request.method]['returns']
        if returns:
            response = self._call_registered_method(request.method, message_id, *request.args, **request.kwargs)
            payload = pickle.dumps({'data': response, 'request_id': request.request_id})
            self._rds.publish(f'{self._queue_prefix}/response/{request.client_id}', payload)
            self._logger.info(f"Processed message {message_id} and response published to {self._queue_prefix}/response/{request.request_id}")
        else:
            self._call_registered_method_no_returns(request.method, message_id, *request.args, **request.kwargs)
            self._logger.info(f"Processed message {message_id} without response")


    def _call_registered_method_no_returns(self, method: str, message_id, *args, **kwargs) -> None:
        try:
            self._registered_methods[method]['func'](*args, **kwargs)
            return

        except Exception as e:
            self._logger.error(e)
            return

    def _call_registered_method(self, method: str, message_id, *args, **kwargs) -> Any:
        try:
            message_id = message_id.decode('utf-8') if isinstance(message_id, bytes) else message_id

            data = self._registered_methods[method]['func'](*args, **kwargs)

            response = Response(self._service, message_id)
            response.data = data
            return response
        except Exception as e:
            self._logger.error(e)
            response = Response(self._service, message_id, status='error', error=str(e))
            return response
