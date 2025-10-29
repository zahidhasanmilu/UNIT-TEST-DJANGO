from django.urls import path
from documentation import views


urlpatterns = [
    path('list_of_documentation/', views.documentation_list, name='documentation_list'),
    path('<uuid:pk>/', views.documentation_detail, name='documentation_detail'),
]
