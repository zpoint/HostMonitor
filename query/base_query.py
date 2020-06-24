# -*- coding: utf-8 -*-
import abc


class Query(object):
    def __init__(self, parsed_param):
        self.param = parsed_param

    @abc.abstractmethod
    async def create_meta(self):
        """
        create meta data according to param
        :return:
        """
        pass

    @abc.abstractmethod
    async def create_data(self):
        """
        create data according to param
        :return:
        """
        pass

    @abc.abstractmethod
    async def search_meta(self):
        """
        search meta data
        :return:
        """
        pass

    @abc.abstractmethod
    async def search_data(self):
        """
        search data
        :return:
        """
        pass

    @abc.abstractmethod
    async def update_meta(self):
        """
        update meta data
        :return:
        """
        pass

    @abc.abstractmethod
    async def update_data(self):
        """
        update data
        :return:
        """
        pass

    @abc.abstractmethod
    async def delete_meta(self):
        """
        delete meta data
        :return:
        """
        pass

    @abc.abstractmethod
    async def delete_data(self):
        """
        delete data
        :return:
        """
        pass

    @abc.abstractmethod
    async def list(self):
        """
        show cluster info
        :return:
        """
        pass
