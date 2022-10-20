from aiohttp import web
from .views import home, about

routes = [
    web.get('/', home),
    web.get('/about', about)

]