from rest_framework.permissions import BasePermission, SAFE_METHODS

from posts.models import Post, Comment


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj: Post | Comment):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and obj.owner == request.user
