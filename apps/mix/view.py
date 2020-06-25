# -*- coding: utf-8 -*-
from sanic_restplus import Resource
from libs.rest import RestAssoc
from libs.exception import Code
ns = RestAssoc.mix
api = RestAssoc.api
name = "mix"


@ns.route('/node/<region_id:string>')
class MixNodes(Resource):
    @ns.doc('list_all')
    async def get(self, request):
        """
        list all nodes in ElasticSearch and InfluxDB in specific region
        """
        raise Code.CurrentlyNotSupport


@ns.route('/resource/<keyword:string>')
class MixNodes(Resource):
    @ns.doc('list_all')
    async def get(self, request):
        """
        list all index contains "keyword" and all measurement contains "keyword"
        """
        raise Code.CurrentlyNotSupport
