import jinja2
from aiohttp import web
from app.routes import routes
import asyncio
import aiohttp_jinja2
from app.settings import BASE_DIR, get_config
from app.store.database.accessor import PostgresAccessor


async def timer(app):
    while True:
        await asyncio.sleep(1)
        print(app)

if __name__ == '__main__':
    app = web.Application()

    app['config'] = get_config
    app["db"]

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(''))

    app.add_routes(routes)

    app.on_startup.append(timer)

    web.run_app(
        app,
        port=app["config"]["common"]["port"],
        host=app["config"]["common"]["host"]
    )