from django.contrib.auth import get_backends
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import *
# Create your views here.


class PostListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostCreateView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    # queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):

        # note: you cannot call .save() after accessing serializer.data
        # print(serializer.data)
        serializer.save(user=self.request.user)


class PostUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
