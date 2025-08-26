from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Post, Tag, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.username", read_only=True)
    new_tags = serializers.ListField(child=serializers.CharField(), required=False, write_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "image", "created_at", "updated_at", "owner", "new_tags"]
        read_only_fields = ["id", "created_at", "updated_at", "owner"]
        extra_kwargs = {
            "content": {"write_only": True},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    # post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), required=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "created_at", "updated_at", "owner", "post"]
        read_only_fields = ["created_at", "updated_at", "owner", "id"]


class PostDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    tags_list = serializers.ListSerializer(source="tags", child=serializers.CharField(), read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "image", "created_at", "updated_at", "owner", "tags_list"]
        read_only_fields = ["id", "created_at", "updated_at", "owner"]
