# -*- coding: utf-8 -*-

from config.basic import BasicSettings


class Settings(BasicSettings):
    ES_HOSTS: list = ["bw", ]

    INFLUX_HOST = ""
    INFLUX_PORT = ""
