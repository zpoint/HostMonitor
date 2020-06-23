# -*- coding: utf-8 -*-
from sanic import Sanic
from environs import Env
from config.settings import Settings, args, debug
from libs.middlewares import setup_middlewares
from libs.http_util import setup_http
from libs.exception import customer_exception_handler
from libs.logs import get_log_config
from routes import setup_routes

if __name__ == "__main__":
    env = Env()
    env.read_env()

    log_config = get_log_config(Settings)
    app = Sanic(Settings.PROJECT_NAME, log_config=log_config)
    app.config.from_object(Settings)

    setup_routes(app)
    setup_http(app)
    setup_middlewares(app)
    app.error_handler.add(Exception, customer_exception_handler)

    app.run(
        host=args.host,
        port=args.port,
        debug=debug,
        access_log=debug,
        workers=args.workers,
        auto_reload=debug,
    )
