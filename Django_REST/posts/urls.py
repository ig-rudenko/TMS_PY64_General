from django.urls import path

from posts.views import PostsListView, create_post_view, post_detail_view, edit_post_view, add_comment_view

# /posts/
urlpatterns = [
    path("", PostsListView.as_view(), name="posts-list"),
    path("create", create_post_view, name="post-create"),
    path("<int:post_id>", post_detail_view, name="post-view"),
    path("<int:post_id>/edit", edit_post_view, name="post-edit"),
    path("<int:post_id>/add-comment", add_comment_view, name="post-add-comment"),
]
