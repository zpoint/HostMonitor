# -*- coding: utf-8 -*-
from collections import namedtuple
import sanic_restplus.api
from spf import SanicPluginsFramework
from sanic_restplus.restplus import restplus
from sanic_restplus import Api, namespace
from libs.exception import customer_rest_exception_handler

"""
Dismiss unwanted exception
"""


class ApiErrorHandler(sanic_restplus.api.ErrorHandler):
    def __init__(self, original_handler, api):
        super(ApiErrorHandler, self).__init__()
        self.original_handler = original_handler
        self.api = api

    def response(self, request, e1):
        return self.original_handler.response(request, e1)


sanic_restplus.api.ApiErrorHandler = ApiErrorHandler


class RestAssoc(object):
    rest_assoc: namedtuple = None
    api: Api = Api(version='1.0', title='HostMonitor API',
                   description='monitor metadata of influxdb and ES, rest api support for CRUD metadata and results')
    ns_es: namespace = api.namespace('es', description='ElasticSearch operations')
    api._default_error_handler = customer_rest_exception_handler


def setup_rest(app):
    spf = SanicPluginsFramework(app)
    rest_assoc = spf.register_plugin(restplus)
    RestAssoc.rest_assoc = rest_assoc
    RestAssoc.rest_assoc.api(RestAssoc.api)
