# -*- coding: utf-8 -*-
import abc
from libs.code import Code


class Query(object):
    def __init__(self, parsed_param):
        self.param = parsed_param

    async def create_meta(self):
        """
        create meta data according to param
        :return:
        """
        raise Code.CurrentlyNotSupport

    async def create_data(self):
        """
        create data according to param
        :return:
        """
        raise Code.CurrentlyNotSupport

    async def search_meta(self):
        """
        search meta data
        :return:
        """
        raise Code.CurrentlyNotSupport

    async def search_data(self):
        """
        search data
        :return:
        """
        raise Code.CurrentlyNotSupport

    async def update_meta(self):
        """
        update meta data
        :return:
        """
        raise Code.CurrentlyNotSupport

    async def insert_meta(self):
        """
        insert meta data
        :return:
        """
        raise Code.CurrentlyNotSupport

    async def update_data(self):
        """
        update data
        :return:
        """
        raise Code.CurrentlyNotSupport

    async def delete_meta(self):
        """
        delete meta data
        :return:
        """
        raise Code.CurrentlyNotSupport

    async def delete_data(self):
        """
        delete data
        :return:
        """
        raise Code.CurrentlyNotSupport

    @abc.abstractmethod
    async def list(self):
        """
        show cluster info
        :return:
        """
        pass
