# -*- coding: utf-8 -*-

import json
import logging
import traceback
import unittest
from main import app


class ESAutoRestTests(unittest.TestCase):
    index_name = "twitter"

    """Unit testcases for REST APIs"""
    def step1(self):
        # create index
        request, response = app.test_client.post('/es/index', data=json.dumps({'index': self.index_name, 'settings': {'number_of_shards': 1}, 'mappings': {'properties': {'user': {'type': 'text'}, "post_date": {'type': 'date'}, "message": {'type': 'text'}}}}))
        data = json.loads(response.text)
        self.assertEqual(response.status, 200)
        self.assertEqual(data["_index"], self.index_name)

    def step2(self):
        # list index
        request, response = app.test_client.get('/es/index')
        self.assertEqual(response.status, 200)
        data = json.loads(response.text)
        has_index = False
        for each_index in data:
            if each_index["index"] == self.index_name:
                has_index = True
                self.assertEqual(each_index["status"], "open")
        self.assertTrue(has_index)

    def step3(self):
        # list nodes
        request, response = app.test_client.get('/es/node')
        self.assertEqual(response.status, 200)
        data = json.loads(response.text)
        self.assertIn("cluster_name", data)
        self.assertIn("nodes", data)
        logging.info("cluster_name: %s" % (data["cluster_name"], ))

    def step4(self):
        # insert data
        request, response = app.test_client.put('/es/%s' % (self.index_name, ), data=json.dumps({"user": "kimchy", "post_date": "2009-11-15T14:12:12", "message": "trying out Elasticsearch"}))
        self.assertEqual(response.status, 200)
        data = json.loads(response.text)
        self.assertEqual(data["result"], "created")

    def step5(self):
        # search data
        request, response = app.test_client.get('/es/%s' % (self.index_name, ))
        self.assertEqual(response.status, 200)

    def step6(self):
        # delete_index
        request, response = app.test_client.delete('/es/%s' % (self.index_name, ))
        self.assertEqual(response.status, 200)

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


if __name__ == '__main__':
    unittest.main()
