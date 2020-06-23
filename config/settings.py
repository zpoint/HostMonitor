# -*- coding: utf-8 -*-
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
