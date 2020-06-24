# -*- coding: utf-8 -*-
from sanic_envconfig import EnvConfig


class BasicSettings(EnvConfig):
    DEBUG: bool = True
    HOST: str = 'localhost'
    PORT: int = 8000
    WORKERS: int = 1
    PROJECT_NAME: str = "HostMonitor"
    KEEP_ALIVE_TIMEOUT: int = 20

    HTTP_REQUEST_CONCURRENCY_LIMIT: int = 50

