# -*- coding: utf-8 -*-

from config.basic import BasicSettings


class Settings(BasicSettings):
    # ES_HOSTS: list = ["bw:10000", ]
    ES_HOSTS: list = ["es_dev", ]

    INFLUX_HOST = ""
    INFLUX_PORT = ""
