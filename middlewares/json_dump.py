# -*- coding: utf-8 -*-
from sanic.response import json, HTTPResponse
from libs.code import Code
from libs.useful import my_json_dump


def json_dump_middleware(request, response):
    if not isinstance(response, HTTPResponse):
        response = HTTPResponse(
            json({
                "result": True,
                "resultcode": Code.SUCCESS,
                "msg": '',
                "errormsg": '',
                "data": response if response else {},
            }, status=200, dumps=my_json_dump).body,
            content_type="application/json",
        )
    return response
