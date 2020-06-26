# -*- coding: utf-8 -*-
from sanic import Sanic
from environs import Env
from config.settings import Settings, args, debug, env_cover
from libs.middlewares import setup_middlewares
from libs.exception import customer_exception_handler
from libs.http_util import setup_http
from libs.db_util import setup_database
from libs.logs import get_log_config
from libs.rest import setup_rest
from routes import setup_routes

"""
unittest need to move app statement to main block
"""
env = Env()
env.read_env()
env_cover()
log_config = get_log_config(Settings)
app = Sanic(Settings.PROJECT_NAME, log_config=log_config)
app.config.from_object(Settings)

setup_database(app)
setup_http(app)
setup_middlewares(app)
app.error_handler.add(Exception, customer_exception_handler)
setup_rest(app)
setup_routes(app)

if __name__ == "__main__":
    app.run(
        host=Settings.HOST or args.host,
        port=args.port,
        debug=debug,
        access_log=debug,
        workers=args.workers,
        auto_reload=debug,
    )
