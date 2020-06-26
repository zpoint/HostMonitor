# -*- coding: utf-8 -*-
from libs.resource import InfluxResource
from libs.rest import RestAssoc
from libs.exception import Code
ns = RestAssoc.ns_influx
api = RestAssoc.api
name = "influx"


@ns.route('/node')
class InFluxNodes(InfluxResource):
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
class InFluxDBs(InfluxResource):
    @ns.doc('list_all_database')
    async def get(self, request):
        """
        list all databases
        """
        return await self.get_result("list", type="database", measurement="")

    @ns.doc('malloc_new_database')
    @ns.param("json body", "json body", _in="body", example={"db": "testdb"})
    async def post(self, request):
        """
        create a new database
        """
        return await self.get_result("create_meta", request.json, type="database", **request.json)

    @ns.doc('delete_database')
    @ns.param("json body", "json body", _in="body", example={"db": "testdb"})
    async def delete(self, request):
        """
        drop a database
        """
        return await self.get_result("delete_meta", request.json, type="database", **request.json)


@ns.route('/<db:string>')
@ns.param('db', 'The database name', default="testdb")
class InFluxList(InfluxResource):
    @ns.doc('list_all_measurement')
    async def get(self, request, db):
        """
        list all measurements in a db
        """
        return await self.get_result("list", db=db, type="measurement")

    @ns.doc('create_new_db')
    async def put(self, request, db):
        """
        create a new database in a db
        """
        return await self.get_result("create_meta", db=db, type="database")

    @ns.doc('delete_given_database')
    async def delete(self, request, db):
        """
        delete a given database
        """
        return await self.get_result("delete_meta", db=db, type="database")


@ns.route('/<db:string>/<measurement:string>')
@ns.param('db', 'The database name', default="testdb")
@ns.param('measurement', 'The measurement name', default="cpu_load")
class InFluxList(InfluxResource):
    @ns.doc('create_new_measurement')
    @ns.param("json body", "json body", _in="body", example={
        'time': '2009-11-10T23:00:00Z',
        'tags': {
            'host': 'server01',
            'region': 'us-west'
        },
        'fields': {'value': 0.64}
    })
    async def put(self, request, db, measurement):
        """
        create a new measurement in a db
        """
        return await self.get_result("create_meta", request.json, db=db, measurement=measurement, type="measurement")

    @ns.doc('delete_given_measurement')
    async def delete(self, request, db, measurement):
        """
        delete a given measurement
        """
        return await self.get_result("delete_meta", db=db, measurement=measurement, type="measurement")

    @ns.doc('get_field')
    async def get(self, request, db, measurement):
        """list all tag_keys and field_keys in a measurement"""
        return await self.get_result("list", request.json, db=db, measurement=measurement, type="field")
