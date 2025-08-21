from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.services import get_posts_list
from .serializers import PostSerializer


class PostListCreateAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # http://127.0.0.1:8000/posts/?search=python
        # search: str = request.GET.get("search", "")  # python
        qs = get_posts_list(
            search=self.request.GET.get("search", ""),
            username_search=self.request.GET.get("user", ""),
            tags=self.request.GET.get("tags", []),
        )
        return qs

    def perform_create(self, serializer):
        print("self.request.data =", self.request.data)
        print("type(self.request.data) =", type(self.request.data))
        serializer.save(owner=self.request.user)
