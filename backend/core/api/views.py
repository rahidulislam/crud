from urllib import request
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from core.models import Post
from core.api.serializers import PostCreateSerializer, PostSerializer
from core.api.petmissions import AuthorOrReadOnly


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    

class PostCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset=Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer