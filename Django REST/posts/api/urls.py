from django.urls import path

from posts.api.views import (
    PostListCreateAPIView,
    PostDetailAPIView,
    CommentListCreateAPIView,
    CommentDetailAPIView,
    ImageUploadAPIView,
    CharCounterAPIView,
    TaskResultAPIView,
)

# /api/v1/

app_name = "api"

urlpatterns = [
    path("posts", PostListCreateAPIView.as_view(), name="posts-list-create"),
    path("posts/<int:id>", PostDetailAPIView.as_view()),
    path("comments", CommentListCreateAPIView.as_view()),
    path("comments/<int:id>", CommentDetailAPIView.as_view()),
    path("upload/image", ImageUploadAPIView.as_view(), name="image-upload"),
    path("tasks/char-counter", CharCounterAPIView.as_view(), name="char-counter"),
    path("tasks/results", TaskResultAPIView.as_view(), name="task-result"),
]
