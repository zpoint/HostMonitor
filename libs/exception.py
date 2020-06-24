# -*- coding: utf-8 -*-
import traceback
from sanic import response
from libs.code import ValidationError, Code


def customer_exception_handler(request, exception):
    if isinstance(exception, ValidationError):
        data = {
            'result': False,
            'message': exception.message,
            'resultcode': exception.code,
            'data': exception.data
        }
        return response.json(data, status=exception.status_code)
    else:
        errormsg = Code.SYSTEM_ERROR.message
        exc_data = None

        if request and request.app.config.DEBUG:
            errormsg = errormsg + ', err: {}'.format(str(exception))
            traceback.print_exc()
            exc_data = traceback.format_exc()

        data = {
            'result': False,
            'message': errormsg,
            'resultcode': Code.SYSTEM_ERROR.code,
            'data': exc_data,
        }
        return response.json(data, status=Code.SYSTEM_ERROR.code)


def customer_rest_exception_handler(exception):
    if isinstance(exception, ValidationError):
        data = {
            'result': False,
            'message': exception.message,
            'resultcode': exception.code,
            'data': exception.data
        }
        return response.json(data, status=exception.status_code)
    else:
        errormsg = Code.SYSTEM_ERROR.message
        exc_data = None

        data = {
            'result': False,
            'message': errormsg,
            'resultcode': Code.SYSTEM_ERROR.code,
            'data': exc_data,
        }
        return response.json(data, status=Code.SYSTEM_ERROR.code)
