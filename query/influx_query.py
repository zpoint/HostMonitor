# -*- coding: utf-8 -*-
from .base_query import Query
from libs.db_util import DBUtil
from libs.code import Code


class InfluxQuery(Query):
    def __init__(self, parsed_param):
        super().__init__(parsed_param)
        self.db_instance = DBUtil.influxdb[parsed_param["db"]]

    async def create_meta(self, type_="database"):
        """
        create meta data according to param
        :return:
        """
        if type_ == "database":
            db = self.param["db"]
            return await self.db_instance.create_database(db=db)
        raise NotImplementedError("type: %s not implemented" % (type_, ))

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
        pass

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

    async def delete_meta(self, type_="database"):
        """
        delete meta data
        :return:
        """
        if type_ == "database":
            db = self.param["db"]
            return await self.db_instance.drop_database(db=db)
        raise NotImplementedError("type: %s not implemented" % (type_,))

    async def delete_data(self):
        """
        delete data
        :return:
        """
        pass

    async def list(self, type_="database"):
        """
        show cluster/database info
        :return:
        """
        if type_ == "database":
            return await self.db_instance.show_databases()
        raise NotImplementedError("type: %s not implemented" % (type_, ))
