from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView)

from news.serializers import PostSerializer
from news.models import Post

# Create your views here.


class PostCreateView(CreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class PostUpdateView(UpdateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


class PostDeleteView(DestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


class PostsListView(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

