from aiohttp import web
from . import views


routes = [
    web.get('/', views.Index, name='index'),
    web.rote('*', '/chat/rooms', views.CreateRoom, name='create_room')
]