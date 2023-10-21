from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('messages/', views.messages, name='blog-messages'),
    path('article/', views.article, name="blog-article")
]

