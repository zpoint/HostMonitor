# -*- coding: utf-8 -*-
import json
import datetime


def my_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


def my_json_dump(*args, **kwargs):
    kwargs["default"] = my_converter
    return json.dumps(*args, **kwargs)
