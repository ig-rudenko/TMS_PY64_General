from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "title", "content", "image", "created_at", "updated_at", "owner"]
        read_only_fields = ["id", "created_at", "updated_at", "owner"]


s = PostSerializer(data={"title": "NEW123", "content": "jofhuisdhfui"})
s.is_valid(raise_exception=True)
