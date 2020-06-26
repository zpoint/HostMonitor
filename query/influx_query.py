# -*- coding: utf-8 -*-
import aioinflux.client
from .base_query import Query
from libs.db_util import DBUtil
from libs.code import Code


class InfluxQuery(Query):
    def __init__(self, meta_param: dict, parsed_query_param: dict):
        super().__init__(meta_param, parsed_query_param)
        self.db = meta_param["db"] if "db" in meta_param else "default"
        self.db_instance = DBUtil.influxdb[self.db]

    async def create_meta(self):
        """
        create meta data according to param
        :return:
        """
        if self.type_ == "database":
            return await self.db_instance.create_database(db=self.db)
        elif self.type_ == "measurement":
            try:
                res = await self.db_instance.write(self.parsed_query_param)
                return {"result": res}
            except aioinflux.client.InfluxDBWriteError:
                raise Code.DBNotExist(self.db)
        raise NotImplementedError("type: %s not implemented" % (self.type_, ))

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

    async def delete_meta(self):
        """
        delete meta data
        :return:
        """
        if self.type_ == "database":
            return await self.db_instance.drop_database(db=self.db)
        elif self.type_ == "measurement":
            measurement = self.meta_param["measurement"]
            try:
                res = await self.db_instance.drop_measurement(measurement)
                return res
            except aioinflux.client.InfluxDBWriteError:
                raise Code.DBNotExist(self.db)
        raise NotImplementedError("type: %s not implemented" % (self.type_, ))

    async def delete_data(self):
        """
        delete data
        :return:
        """
        pass

    async def list(self):
        """
        show cluster/database info
        :return:
        """
        if self.type_ == "database":
            return await self.db_instance.show_databases()
        elif self.type_ == "measurement":
            return await self.db_instance.show_measurements()
        elif self.type_ == "field":
            try:
                res1 = await self.db_instance.show_tag_keys(self.meta_param["measurement"])
                res1 = res1["results"][0]["series"][0]
                res2 = await self.db_instance.show_field_keys(self.meta_param["measurement"])
                res2 = res2["results"][0]["series"][0]
                result = {"tag_keys": res1, "field_keys": res2}
                return result
            except aioinflux.client.InfluxDBError:
                raise Code.DBNotExist(self.db)
        raise NotImplementedError("type: %s not implemented" % (self.type_, ))
