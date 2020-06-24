# -*- coding: utf-8 -*-
from aioelasticsearch import Elasticsearch


class DBUtil(object):
    es: Elasticsearch = None


async def setup_db(app, loop):
    DBUtil.es = Elasticsearch(hosts=app.config.ES_HOSTS)


async def close_db(app, loop):
    await DBUtil.es.close()


def setup_database(app):
    app.register_listener(setup_db, 'before_server_start')
    app.register_listener(close_db, 'before_server_stop')
