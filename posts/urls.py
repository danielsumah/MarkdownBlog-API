from django.urls import path, include
from rest_framework.generics import RetrieveAPIView
from .views import *

app_name = 'posts'
urlpatterns = [
    path('posts/', PostListView.as_view(), name="posts-url"),
    path('post/<slug>/', PostDetailView.as_view(), name="get-post-url"),
]
