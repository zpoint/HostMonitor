# -*- coding: utf-8 -*-
import os
import sys


def get_log_config(config):
    default_level = 'DEBUG' if config.DEBUG else 'INFO'
    log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), './logs')

    if not os.path.exists(log_path):
        os.mkdir(log_path, mode=0o755)

    return {
        'version': 1,
        'disable_existing_loggers': False,
        'loggers': {
            'sanic.root': {
                'level': default_level,
                'handlers': ['console'],
            },
            'sanic.error': {
                'level': default_level,
                'handlers': ['access', 'console'],
                'propagate': True,
                'qualname': 'sanic.error',
            },
            'sanic.access': {
                'level': default_level,
                'handlers': ['access', 'console'],
                'propagate': True,
                'qualname': 'sanic.access',
            },
            'apps': {
                'level': default_level,
                'handlers': ['apps', 'console'],
                'propagate': True,
                'qualname': 'apps',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'generic',
                'stream': sys.stdout,
            },
            'access': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'access',
                'filename': '{}/access.log'.format(log_path),
                'maxBytes': 50 * 1024 * 1024,
            },
            'apps': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'generic',
                'filename': '{}/app.log'.format(log_path),
                'maxBytes': 50 * 1024 * 1024,
            }
        },
        'formatters': {
            'generic': {
                'format': '[%(asctime)s] [%(name)s.%(module)s.%(funcName)s:%(lineno)s] %(levelname)s: %(message)s',
                'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
                'class': 'logging.Formatter',
            },
            'access': {
                'format': '[%(asctime)s] [%(name)s.%(module)s.%(funcName)s:%(lineno)s] %(levelname)s: %(message)s',
                'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
                'class': 'logging.Formatter',
            },
        },
    }
