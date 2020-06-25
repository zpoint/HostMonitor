# -*- coding: utf-8 -*-
import json
from sanic_restplus import reqparse
from sanic_restplus import Resource
from libs.rest import RestAssoc
from libs.exception import Code
from query.query_factory import QueryFactory
ns = RestAssoc.ns_es
api = RestAssoc.api
name = "es"


@ns.route('/nodes')
class ESNodes(Resource):
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


@ns.route('/index')
class ESList(Resource):
    @ns.doc('list_all_index')
    async def get(self, request):
        """
        list all indexes in a cluster
        """
        query = QueryFactory.create_query(name, request.json)
        return await query.search_meta()

    @ns.doc('create_new_index')
    @ns.param("json body", "json body", _in="body", example={
        "index": "twitter", 'settings': {'number_of_shards': 1},
        'mappings': {'properties': {'field1': {'type': 'text'}}}})
    async def put(self, request):
        """
        create a new index in a cluster
        """
        json_body = {"index": request.json["index"], "body": request.json}
        del request.json["index"]
        query = QueryFactory.create_query(name, json_body)
        return await query.insert_meta()

    @ns.doc('delete_given_index')
    @ns.param("index", "index name", _in="query", default="twitter")
    async def delete(self, request):
        """
        delete a given index
        """
        query_dict = dict(request.query_args)
        query = QueryFactory.create_query(name, query_dict)
        res = await query.delete_meta()
        if "status" in res:
            return res, res["status"]
        else:
            return res


@ns.route('/<index:string>')
@ns.param('index', 'The index name')
class ESData(Resource):
    """act as a proxy and delegate your CRUD query to the real backend"""

    @ns.doc('get_data')
    async def get(self, request, index):
        """Fetch given resource"""
        request.json["index"] = index
        query = QueryFactory.create_query(name, request.json)
        return await query.search_data()

    @ns.doc('delete_data')
    async def delete(self, request, index):
        """Delete data in a given index by it's query"""
        request.json["index"] = index
        query = QueryFactory.create_query(name, request.json)
        return await query.delete_data()

    @ns.doc('update_data')
    async def put(self, request, index):
        """forward DSL to given index"""
        request.json["index"] = index
        query = QueryFactory.create_query(name, request.json)
        return await query.update_data()
