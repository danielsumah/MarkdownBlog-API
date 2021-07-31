from django.urls import path, include
from rest_framework.generics import RetrieveAPIView
from .views import *

app_name = 'posts'
urlpatterns = [
    path('', home_view, name='home'),
    path('api/posts/', PostListView.as_view(), name="posts-url"),
    path('api/post/create/', PostCreateView.as_view(), name="create-post"),
    path('api/post/<slug>/', PostDetailView.as_view(), name="get-post-url"),
    path('api/post/<slug>/update/',
         PostUpdateView.as_view(), name="update-post-url"),
    path('api/post/<slug>/delete/',
         PostDeleteView.as_view(), name="delete-post-url"),
    # path('post/users/', GetUserView.as_view(), name="get-user-url"),
]
