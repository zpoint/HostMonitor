# -*- coding: utf-8 -*-

import json
import logging
import traceback
import unittest
from aioinflux import InfluxDBClient
from config.settings import Settings
from libs.db_util import DBUtil
from main import app

"""
unittest 下单例模式报 eventloop.close 错误
"""


class InfluxdbDict(dict):
    def __getitem__(self, item: str) -> InfluxDBClient:
        db_instance = InfluxDBClient(host=Settings.INFLUX_HOST, port=Settings.INFLUX_PORT, db=item)
        return db_instance


DBUtil.influxdb = InfluxdbDict()


class InfluxAutoRestTestsBase(unittest.TestCase):
    database_name = "my_db"
    measurement_name = "cpu_load"

    def _steps(self):
        for name in dir(self):  # dir() result is implicitly sorted
            if name.startswith("step"):
                yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self._steps():
            try:
                step()
            except Exception as e:
                logging.error(traceback.format_exc())
                self.fail("{} failed ({}: {})".format(step, type(e), e))


class InfluxAutoRestTests(InfluxAutoRestTestsBase):
    """Unit testcases for REST APIs"""
    def step1(self):
        # create database
        request, response = app.test_client.put('/influx/%s' % (self.database_name, ))
        data = json.loads(response.text)
        self.assertEqual(response.status, 200)
        self.assertIn("results", data)

    def step2(self):
        # list database
        request, response = app.test_client.get('/influx/db')
        data = json.loads(response.text)
        self.assertEqual(response.status, 200)
        res = (i[0] for i in data["results"][0]["series"][0]["values"])
        self.assertIn(self.database_name, res)

    def step3(self):
        # create a new measurement
        data = {'time': '2009-11-10T23:00:00Z', 'tags': {'host': 'server01', 'region': 'us-west'},
                'fields': {'value': 0.64}}
        request, response = app.test_client.put('/influx/%s/%s' % (self.database_name, self.measurement_name),
                                                data=json.dumps(data))
        data = json.loads(response.text)
        self.assertEqual(response.status, 200)
        self.assertEqual({"result": True}, data)

    def step4(self):
        # list all field keys and tag keys
        request, response = app.test_client.get('/influx/%s/%s' % (self.database_name, self.measurement_name))
        data = json.loads(response.text)
        print("data", data)
        tag_keys = {i[0] for i in data["tag_keys"]["values"]}
        field_keys = data["field_keys"]["values"][0]
        self.assertIn("host", tag_keys)
        self.assertIn("region", tag_keys)
        self.assertIn("value", field_keys)
        self.assertIn("float", field_keys)

    def step5(self):
        # delete measurement
        request, response = app.test_client.delete('/influx/%s/%s' % (self.database_name, self.measurement_name))
        data = json.loads(response.text)
        self.assertEqual(response.status, 200)

    def step6(self):
        # drop database
        request, response = app.test_client.delete('/influx/%s' % (self.database_name,))
        data = json.loads(response.text)
        self.assertEqual(response.status, 200)
        self.assertIn("results", data)


if __name__ == '__main__':
    unittest.main()
