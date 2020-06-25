# -*- coding: utf-8 -*-
from sanic_restplus import Resource
from operator_.operator import Operator
from parser.json_body_parser import ESJsonBodyParser, InfluxJsonBodyParser, MixJsonBodyParser


class MyResource(Resource):
    parser = ESJsonBodyParser

    async def get_result(self, action: str, request_json: dict = None, **kwargs):
        """
        :param action:
        :param request_json:
        :param kwargs: meta
        :return:
        """
        parser = self.parser(action, request_json, **kwargs)
        op = Operator(parser.result())
        res = await op.operate()
        if isinstance(res, dict):
            if "status" in res:
                return res, res["status"]
        return res


class ESResource(MyResource):
    parser = ESJsonBodyParser


class InfluxResource(MyResource):
    parser = InfluxJsonBodyParser


class MixResource(MyResource):
    parser = MixJsonBodyParser
