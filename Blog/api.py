from rest_framework import viewsets, permissions
from Blog.models import Post
from Blog.serializers import PostSerializer,CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objetcts.all()
    serializer_class = PostSerializer
    permission_class = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Post.objetcts.all()
    serializer_class = CommentSerializer
    permission_class = [permissions.IsAuthenticated]