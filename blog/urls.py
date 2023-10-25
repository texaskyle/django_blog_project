from django.urls import path
from blog.views import PostListView
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('messages/', views.messages, name='blog-messages'),
    path('article/', views.article, name="blog-article")
]

