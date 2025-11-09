from django.urls import path
from . import views

urlpatterns = [
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee/<uuid:pk>/', views.employee_detail, name='employee_detail'),
    path('employee/create/', views.employee_create, name='employee_create'),
]
