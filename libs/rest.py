# -*- coding: utf-8 -*-
from collections import namedtuple
from spf import SanicPluginsFramework
from sanic_restplus.restplus import restplus
from sanic_restplus import Api, namespace


class RestAssoc(object):
    rest_assoc: namedtuple = None
    api: Api = Api(version='1.0', title='HostMonitor API',
                   description='monitor metadata of influxdb and ES, rest api support for CRUD metadata and results')
    ns_es: namespace = api.namespace('es', description='ElasticSearch operations')


def setup_rest(app):
    spf = SanicPluginsFramework(app)
    rest_assoc = spf.register_plugin(restplus)
    RestAssoc.rest_assoc = rest_assoc
    RestAssoc.rest_assoc.api(RestAssoc.api)
