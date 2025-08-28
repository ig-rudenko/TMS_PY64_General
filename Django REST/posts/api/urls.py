from django.urls import path

from posts.api.views import (
    PostListCreateAPIView,
    PostDetailAPIView,
    CommentListCreateAPIView,
    CommentDetailAPIView,
    ImageUploadAPIView,
)

# /api/v1/

urlpatterns = [
    path("posts", PostListCreateAPIView.as_view(), name="posts-list"),
    path("posts/<int:id>", PostDetailAPIView.as_view()),
    path("comments", CommentListCreateAPIView.as_view()),
    path("comments/<int:id>", CommentDetailAPIView.as_view()),
    path("upload/image", ImageUploadAPIView.as_view(), name="image-upload"),
]
