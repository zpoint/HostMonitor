# -*- coding: utf-8 -*-
from .base_query import Query
from libs.db_util import DBUtil


class ESQuery(Query):
    async def create_meta(self):
        """
        create meta data according to param
        :return:
        """
        index = self.param["index"]
        body = self.param["body"]
        return await DBUtil.es.index(index, body)

    async def create_data(self):
        """
        create data according to param
        :return:
        """
        pass

    async def search_meta(self):
        """
        search meta data
        :return:
        """
        return await DBUtil.es.cat.indices(format="json")

    async def search_data(self):
        """
        search data
        :return:
        """
        pass

    async def update_meta(self):
        """
        update meta data
        :return:
        """
        pass

    async def update_data(self):
        """
        update data
        :return:
        """
        pass

    async def delete_meta(self):
        """
        delete meta data
        :return:
        """
        index = self.param["index"]
        return await DBUtil.es.indices.delete(index=index, ignore=[400, 404])

    async def delete_data(self):
        """
        delete data
        :return:
        """
        pass

    async def list(self, type_="cluster"):
        """
        show cluster info
        :return:
        """
        return await DBUtil.es.nodes.info()
