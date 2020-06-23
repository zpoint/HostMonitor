# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger('sanic.root')


async def hello(request):
    return {"hello": "world"}


def setup_routes(app):
    app.add_route(hello, "/")
    app.add_route(hello, "/favicon.ico")
    for handler, (rule, router) in app.router.routes_names.items():
        logger.info("register rule: %s with handler: %s" % (str(rule), str(handler)))
