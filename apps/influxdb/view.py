# -*- coding: utf-8 -*-
from sanic_restplus import Resource
from libs.rest import RestAssoc
from libs.exception import Code
from query.query_factory import QueryFactory
ns = RestAssoc.ns_influx
api = RestAssoc.api
name = "influx"


@ns.route('/node')
class InFluxNodes(Resource):
    @ns.doc('list_all')
    async def get(self, request):
        """
        list all nodes in a cluster(Not implemented yet, The free version does not support cluster(太穷了😢))
        """
        raise Code.CurrentlyNotSupport

    @ns.doc('malloc_new_node')
    async def post(self, request):
        """
        malloc a new node for current cluster(Not implemented yet)
        """
        raise Code.CurrentlyNotSupport


@ns.route('/db')
class InFluxDBs(Resource):
    @ns.doc('list_all_database')
    async def get(self, request):
        """
        list all databases
        """
        query = QueryFactory.create_query(name, {"db": "default"})
        return await query.list()

    @ns.doc('malloc_new_database')
    @ns.param("json body", "json body", _in="body", example={"db": "testdb"})
    async def post(self, request):
        """
        create a new database
        """
        query = QueryFactory.create_query(name, request.json)
        return await query.create_meta()

    @ns.doc('delete_database')
    @ns.param("json body", "json body", _in="body", example={"db": "testdb"})
    async def delete(self, request):
        """
        drop a database
        """
        query = QueryFactory.create_query(name, request.json)
        return await query.delete_meta()


@ns.route('/<db:string>/<measurement:string>')
@ns.route('/<db:string>')
class InFluxList(Resource):
    @ns.doc('list_all_measurement')
    async def get(self, request, db, measurement):
        """
        list all measurements in a db
        """
        query = QueryFactory.create_query(name, request.json)
        return await query.search_meta()

    @ns.doc('create_new_measurement')
    async def put(self, request, db, measurement):
        """
        create a new index in a cluster
        """
        json_body = {"index": request.json["index"], "body": request.json}
        del request.json["index"]
        query = QueryFactory.create_query(name, json_body)
        return await query.create_meta()

    @ns.doc('delete_given_index')
    @ns.param("index", "index name", _in="query", default="twitter")
    async def delete(self, request, measurement):
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


@ns.route('/<db:string>/<measurement:string>/crud')
class InFluxData(Resource):
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
        """insert data"""
        request.json["index"] = index
        query = QueryFactory.create_query(name, request.json)
        return await query.update_data()
