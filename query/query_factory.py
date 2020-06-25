# -*- coding: utf-8 -*-
from .base_query import Query
from .es_query import ESQuery
from .influx_query import InfluxQuery


class QueryFactory(object):
    @staticmethod
    def create_query(name: str, param: dict = None) -> Query:
        if "es" in name.lower():
            return ESQuery(param)
        elif "influx" in name.lower():
            return InfluxQuery(param)
        raise NotImplementedError("query: %s not implemented" % (name, ))
