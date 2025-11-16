import os
from channels.routing import ProtocolTypeRouter, URLRouter # ProtocolTypeRouter is key
from django.core.asgi import get_asgi_application
import documentation.routing # Import your WebSocket routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unit_test_project.settings')

# 1. Get the standard Django ASGI application for HTTP requests
django_asgi_app = get_asgi_application() 

# 2. Define the main application using ProtocolTypeRouter
application = ProtocolTypeRouter({
    "http": django_asgi_app, # HTTP requests go to Django views/middleware
    "websocket": URLRouter( # WebSocket requests go to URLRouter
        documentation.routing.websocket_urlpatterns), # which uses your defined routes
})