# -*- coding: utf-8 -*-
import abc


class BasicParser(object):
    def __init__(self, action: str, body: dict = None, **kwargs):
        """
        :param action: list_meta/search_meta/update_meta/search_data
        :param body: origin query body
        :param kwargs: meta data in rest url, {db: "db1", "measurement": "cpu_load1"}
        """
        self.action = action
        self.origin_body = body if body else dict()
        self.origin_meta = kwargs
        self.result_meta_with_query = dict()
        self.result_query = dict()
        self.parsed = False

    @abc.abstractmethod
    def parse(self):
        pass

    def result(self):
        if not self.parsed:
            self.parse()
        return self.query_name, self.action, self.result_meta_with_query, self.result_query

    @property
    def query_name(self) -> str:
        return ""
