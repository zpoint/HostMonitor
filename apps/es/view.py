# -*- coding: utf-8 -*-
from sanic_restplus import Resource
from libs.rest import RestAssoc
from libs.exception import Code
from query.query_factory import QueryFactory
ns = RestAssoc.ns_es
api = RestAssoc.api
name = "es"


@ns.route('/index')
class ESList(Resource):
    @ns.doc('list_all_index')
    async def get(self, request):
        """
        list all nodes in a cluster
        """
        query = QueryFactory.create_query(name)
        return await query.list()

    @ns.doc('malloc_new_node')
    async def post(self, request):
        """
        malloc a new node for current cluster(not implemented yet)
        """
        raise Code.CurrentlyNotSupport


@ns.route('/nodes')
class ESList(Resource):
    @ns.doc('list_all')
    async def get(self, request):
        """
        list all nodes in a cluster
        """
        query = QueryFactory.create_query(name)
        return await query.list()

    @ns.doc('malloc_new_node')
    async def post(self, request):
        """
        malloc a new node for current cluster(not implemented yet)
        """
        raise Code.CurrentlyNotSupport
