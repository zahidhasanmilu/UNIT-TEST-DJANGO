from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('unit_test.urls')),
    path('employee/', include('app_employee.urls')),
    path('documetation/', include('documentation.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
