from django.urls import path, include
from rest_framework.generics import RetrieveAPIView
from .views import *

app_name = 'posts'
urlpatterns = [
    path('posts/', PostListView.as_view(), name="posts-url"),
    path('post/create/', PostCreateView.as_view(), name="create-post"),
    path('post/<slug>/', PostDetailView.as_view(), name="get-post-url"),
    path('post/<slug>/update/', PostUpdateView.as_view(), name="get-update-url"),
]
