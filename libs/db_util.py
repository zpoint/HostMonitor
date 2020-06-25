# -*- coding: utf-8 -*-
from aioelasticsearch import Elasticsearch
from aioinflux import InfluxDBClient
from config.settings import Settings


class InfluxdbDict(dict):
    def __getitem__(self, item: str) -> InfluxDBClient:
        if item not in self:
            db_instance = InfluxDBClient(host=Settings.INFLUX_HOST, port=Settings.INFLUX_PORT, db=item)
            self.__setitem__(item, db_instance)
        return super().__getitem__(item)


class DBUtil(object):
    es: Elasticsearch = None
    influxdb: InfluxdbDict = InfluxdbDict()


async def setup_db(app, loop):
    DBUtil.es = Elasticsearch(hosts=app.config.ES_HOSTS)
    DBUtil.influxdb["default"] = InfluxDBClient(
        host=Settings.INFLUX_HOST, port=Settings.INFLUX_PORT, db=Settings.INFLUX_DB
    )


async def close_db(app, loop):
    await DBUtil.es.close()
    for v in DBUtil.influxdb.values():
        await v.close()


def setup_database(app):
    app.register_listener(setup_db, 'before_server_start')
    app.register_listener(close_db, 'before_server_stop')
