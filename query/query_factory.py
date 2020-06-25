# -*- coding: utf-8 -*-
from .base_query import Query
from .es_query import ESQuery
from .influx_query import InfluxQuery

QueryMap = {
    "es": ESQuery,
    "influx": InfluxQuery
}


class QueryFactory(object):
    @staticmethod
    def create_query(name: str, meta_param: dict, parsed_query_param: dict) -> Query:
        if name not in QueryMap:
            raise NotImplementedError("query: %s not implemented" % (name, ))
        return QueryMap[name](meta_param, parsed_query_param)
