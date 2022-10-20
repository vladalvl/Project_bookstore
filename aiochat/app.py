import jinja2
from aiohttp import web
import aiohttp_jinja2

if __name__ == '__main__':
    app = web.Application()

    jinja_env = aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(BASE_DIR)
    )