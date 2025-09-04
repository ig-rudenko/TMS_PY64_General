from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework import serializers

from posts.models import Post, Tag, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.username", read_only=True)
    new_tags = serializers.ListField(child=serializers.CharField(), required=False, write_only=True)
    image = serializers.CharField(max_length=512, required=False, allow_null=True)

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


class PostWithViewsCountSerializer(PostDetailSerializer):
    """
    Сериализатор для детального представления поста с количеством просмотров.
    """

    views_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "image",
            "created_at",
            "updated_at",
            "owner",
            "tags_list",
            "views_count",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "owner"]

    def get_views_count(self, obj) -> int:
        """
        Возвращает количество просмотров поста из кэша.

        Использует метод `get_cache_key` из контекста представления (view), чтобы получить уникальный ключ кэша
        для подсчёта просмотров конкретного поста. Если метод доступен и вызываем, то извлекает значение из кэша.
        Если метод отсутствует — возвращает 0.
        """
        # Проверяем, есть ли в контексте сериализатора объект view
        # и есть ли у него метод get_cache_key(), который можно вызвать
        if hasattr(self.context.get("view", {}), "get_cache_key") and callable(
            self.context["view"].get_cache_key
        ):
            # Получаем уникальный ключ кэша для подсчёта просмотров конкретного поста
            cache_key = self.context["view"].get_cache_key()

            # Извлекаем количество просмотров из кэша. Если ключ не существует, возвращаем 0
            return cache.get(cache_key, default=0)

        # Если метод get_cache_key() отсутствует в view, возвращаем 0 как значение по умолчанию
        return 0


class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField(write_only=True)
