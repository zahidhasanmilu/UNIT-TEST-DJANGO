import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
import documentation.routing
from channels.routing import URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unit_test_project.settings')

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    "http": django_asgi_app, 
    "websocket": URLRouter(
        documentation.routing.websocket_urlpatterns), 
})