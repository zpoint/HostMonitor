# -*- coding: utf-8 -*-
import logging
from apps.routes import *
logger = logging.getLogger('sanic.root')


def setup_routes(app):
    for handler, (rule, router) in app.router.routes_names.items():
        logger.info("register rule: %s with handler: %s" % (str(rule), str(handler)))
