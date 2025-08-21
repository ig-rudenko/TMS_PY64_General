from django.urls import path

from posts.api.views import PostListCreateAPIView


# /api/v1/

urlpatterns = [
    path("posts", PostListCreateAPIView.as_view(), name="posts-list"),
    # path("comments", CommentsListAPIView),
]
