from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('blogs/', views.blogs_list, name='blogs_list'),
    path('blogs/create/', views.create_blog, name='create_blog'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blogs/<slug:slug>/update/', views.blog_update, name='blog_update'),
    
]