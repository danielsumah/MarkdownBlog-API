from django.urls import path, include
from .views import *

app_name = 'posts'
urlpatterns = [
    path('posts/', PostListView.as_view(), name="posts-url")
]
