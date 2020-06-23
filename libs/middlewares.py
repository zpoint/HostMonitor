# -*- coding: utf-8 -*-
from sanic.response import json, HTTPResponse
from libs.code import Code
from libs.useful import my_json_dump
from middlewares.auth import authenticate
from middlewares.json_dump import json_dump_middleware


def setup_middlewares(app):
    app.register_middleware(authenticate, 'request')
    app.register_middleware(json_dump_middleware, 'response')
