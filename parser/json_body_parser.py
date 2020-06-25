# -*- coding: utf-8 -*-
from libs.code import Code
from .basic_parser import BasicParser


class JsonBodyParser(BasicParser):
    CONSTANT_META_KEY = set()
    NEED_IN_QUERY_META_KEY = set()
    NO_REPORT_PARAM_ERROR_KEYS = {"type", }
    """
    For ES, unpack index, body
    For InfluxDB, unpack db, measurement, tag, body
    """
    def parse(self):
        # unpack 之后的字典, 包含查询语句和元信息
        result_meta_with_query = dict()
        result_meta_with_query.update(self.origin_body)
        # deep copy if necessary
        # 查询语句, 不包含元信息
        result_query = self.origin_body
        self.verify_parm(result_query, result_meta_with_query)

        self.result_meta_with_query = result_meta_with_query
        self.result_query = result_query
        self.parsed = True

    def verify_parm(self, result_query, result_meta_with_query):
        for key in self.CONSTANT_META_KEY:
            if key in self.origin_meta:
                result_meta_with_query[key] = self.origin_meta[key]
            else:
                if key not in self.NO_REPORT_PARAM_ERROR_KEYS:
                    raise Code.MissingRequiredParam(key)

            if key in self.NEED_IN_QUERY_META_KEY:
                if key in result_meta_with_query:
                    result_query[key] = result_meta_with_query[key]
                if key not in result_query and key not in self.NO_REPORT_PARAM_ERROR_KEYS:
                    raise Code.MissingRequiredParam(key)
            else:
                if key in result_query:
                    del result_query[key]


class ESJsonBodyParser(JsonBodyParser):
    CONSTANT_META_KEY = {"index", "type"}
    NEED_IN_QUERY_META_KEY = {}

    @property
    def query_name(self) -> str:
        return "es"


class InfluxJsonBodyParser(JsonBodyParser):
    CONSTANT_META_KEY = {"db", "measurement", "type"}
    NEED_IN_QUERY_META_KEY = {"measurement", }

    @property
    def query_name(self) -> str:
        return "influx"

    def verify_parm(self, result_query, result_meta_with_query):
        one_in = False
        for key in self.CONSTANT_META_KEY:
            if key in self.origin_meta:
                if key not in self.NO_REPORT_PARAM_ERROR_KEYS:
                    one_in = True
                result_meta_with_query[key] = self.origin_meta[key]

            if key in self.NEED_IN_QUERY_META_KEY:
                if key in result_meta_with_query:
                    result_query[key] = result_meta_with_query[key]
            else:
                if key in result_query:
                    del result_query[key]
        if not one_in:
            raise Code.MissingRequiredParam(str(self.CONSTANT_META_KEY))


class MixJsonBodyParser(JsonBodyParser):
    CONSTANT_META_KEY = {"index", "db", "measurement", "type"}
    NEED_IN_QUERY_META_KEY = {"measurement", }

    @property
    def query_name(self) -> str:
        return "mix"
