# -*- coding: utf-8 -*-
import os
import argparse
from config.basic import BasicSettings

debug = True
parser = argparse.ArgumentParser(description='Run server.')
parser.add_argument('--host', type=str, default=BasicSettings.HOST, help='The host of server bind to.')
parser.add_argument('-p', '--port', type=int, default=BasicSettings.PORT, help='The port of server bind to.')
parser.add_argument('-c', '--workers', type=int, default=BasicSettings.WORKERS, help='The worker nums of server running.')
parser.add_argument('--env', type=str, default="local", help='dev, test or pd', choices=["local", "dev", "test", "pd"])
args = parser.parse_args()
if args.env == "local":
    from config.local import Settings
elif args.env == "dev":
    from config.dev import Settings
elif args.env == "test":
    from config.test import Settings
elif args.env == "pd":
    debug = False
    from config.pd import Settings
else:
    raise ValueError("Unknown env: %s" % (args.env, ))


def env_cover():
    env = os.environ
    if "ES_HOST" in env and "ES_PORT" in env:
        Settings.ES_HOSTS = ["%s:%s" % (env["ES_HOST"], env["ES_PORT"])]
    if "INFLUX_HOST" in env:
        Settings.INFLUX_HOST = env["INFLUX_HOST"]
    if "INFLUX_PORT" in env and isinstance(env["INFLUX_PORT"], str) and env["INFLUX_PORT"].isdigit():
        Settings.INFLUX_PORT = int(env["INFLUX_PORT"])

    if "SERVER_HOST" in env:
        Settings.HOST = env["SERVER_HOST"]
    else:
        Settings.HOST = None
