# -*- coding: utf-8 -*-
from libs.rest import RestAssoc
from libs.exception import Code
from libs.resource import ESResource
ns = RestAssoc.ns_es
api = RestAssoc.api
name = "es"


@ns.route('/node')
class ESNodes(ESResource):
    @ns.doc('list_all')
    async def get(self, request):
        """
        list all nodes in a cluster
        """
        return await self.get_result("list", index="")

    @ns.doc('malloc_new_node')
    async def post(self, request):
        """
        malloc a new node for current cluster(Not implemented yet)
        """
        raise Code.CurrentlyNotSupport


@ns.route('/index')
class ESList(ESResource):
    @ns.doc('list_all_index')
    async def get(self, request):
        """
        list all indexes in a cluster
        """
        return await self.get_result("search_meta", request.json, index="")

    @ns.doc('create_new_index')
    @ns.param("json body", "json body", _in="body", example={
        "index": "twitter", 'settings': {'number_of_shards': 1},
        'mappings': {'properties': {'user': {'type': 'text'}, "post_date": {'type': 'date'}, "message": {'type': 'text'}}}})
    async def post(self, request):
        """
        create a new index in a cluster
        """
        return await self.get_result("create_meta", request.json, index=request.json["index"])

    @ns.doc('delete_given_index')
    @ns.param("index", "index name", _in="query", default="twitter")
    async def delete(self, request):
        """
        delete a given index
        """
        return await self.get_result("delete_meta", **dict(request.query_args))


@ns.route('/<index:string>')
@ns.param('index', 'The index name', default="twitter")
class ESData(ESResource):
    """act as a proxy and delegate your CRUD query to the real backend"""

    @ns.doc('get_data')
    async def get(self, request, index):
        """Fetch given resource"""
        return await self.get_result("search_data", request.json, index=index)

    @ns.doc('delete_index')
    async def delete(self, request, index):
        """Delete a given index"""
        return await self.get_result("delete_meta", index=index)

    @ns.doc('insert_data')
    @ns.param("json body", "json body", _in="body", example={"user": "kimchy", "post_date": "2009-11-15T14:12:12", "message": "trying out Elasticsearch"})
    async def put(self, request, index):
        """Insert document, forward DSL to given index"""
        return await self.get_result("insert_data", request.json, index=index)
