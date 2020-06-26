# -*- coding: utf-8 -*-

from config.basic import BasicSettings


class Settings(BasicSettings):
    ES_HOSTS: list = ["localhost", ]
    # ES_HOSTS: list = ["es_dev", ]

    INFLUX_HOST = "localhost"
    INFLUX_PORT = 8086
    INFLUX_DB = "my_db"
