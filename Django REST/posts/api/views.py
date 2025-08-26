from django.core.cache import cache
from django_filters import rest_framework as filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from posts.services import create_post
from .filters import PostFilter, CommentFilter
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer
from ..models import Post, Comment


class PostListCreateAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().select_related("owner")
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter
    cache_key = "posts_list"
    cache_timeout = 60

    def list(self, request, *args, **kwargs):
        if self.request.GET:
            print("NO USE CACHE")
            return super().list(request, *args, **kwargs)

        cache_data = cache.get(self.cache_key)
        if cache_data is None:
            print("CACHE IS EMPTY")
            # Формируем данные
            cache_data = super().list(request, *args, **kwargs).data
            cache.set(self.cache_key, cache_data, self.cache_timeout)

        return Response(cache_data)

    def perform_create(self, serializer):
        print("self.request.data =", self.request.data)
        print("type(self.request.data) =", type(self.request.data))
        print("serializer.validated_data", serializer.validated_data)
        serializer.instance = create_post(
            title=serializer.validated_data["title"],
            content=serializer.validated_data["content"],
            user=self.request.user,
            image=serializer.validated_data.get("image"),
            new_tags=serializer.validated_data["new_tags"],
        )


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = "id"
    lookup_url_kwarg = "id"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PostDetailSerializer
        return PostSerializer


class CommentListCreateAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all().select_related("owner")
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CommentFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = "id"
    lookup_url_kwarg = "id"
