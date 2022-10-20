import jinja2
from aiohttp import web
from app.routes import routes
import aiohttp_jinja2


@aiohttp_jinja2.tempate('home.html')
async def home(request):
    return {
        'Title': 'Hello, world!',
        'body': ' '
    }


@aiohttp_jinja2.template('home.html')
async def about(request):
    return {
        'Title': 'about',
        'body': str(request.app)
    }