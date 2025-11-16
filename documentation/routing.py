from django.urls import path
from . import consumers # Imports MySyncConsumer




websocket_urlpatterns = [
    # Map the URL path 'ws/sc/' to the MySyncConsumer class
    path("ws/sc/", consumers.MySyncConsumer.as_asgi()), 
    # The .as_asgi() method converts the Consumer class into an ASGI application
    path("ws/ac/", consumers.MyAsyncConsumer.as_asgi()),
]