# -*- coding: utf-8 -*-
import aiohttp
from config.settings import Settings

# http_client = aiohttp.ClientSession()


class HttpUtil(object):
    http_client: aiohttp.ClientSession = None


async def setup_http_session(app, loop):
    session = aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(
            limit=Settings.HTTP_REQUEST_CONCURRENCY_LIMIT, loop=loop
        ),
        loop=loop
    )
    HttpUtil.http_client = session


async def close_http_session(app, loop):
    await HttpUtil.http_client.close()


def setup_http(app):
    app.register_listener(setup_http_session, 'before_server_start')
    app.register_listener(close_http_session, 'before_server_stop')
