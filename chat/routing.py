from django.urls import re_path 
from .consumers import EchoConsumer

websockets_urls=[
    re_path(r"^ws/echo/$",EchoConsumer.as_asgi())
]