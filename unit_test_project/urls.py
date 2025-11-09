from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.conf import settings

# added graphene_django
from graphene_django.views import GraphQLView

from documentation.schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('unit_test.urls')),
    path('employee/', include('employee.urls')),
    path('documetation/', include('documentation.urls')),
    # added graphene_django
    path("graphql/", (GraphQLView.as_view(graphiql=True, schema=schema))),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
