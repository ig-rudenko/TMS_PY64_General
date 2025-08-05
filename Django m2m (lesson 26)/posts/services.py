from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import UploadedFile
from django.db.models import Q, QuerySet

from posts.models import Post, Comment, Tag

User = get_user_model()  # Возвращает модель пользователя текущего проекта.


def get_all_usernames() -> list[str]:
    return list(User.objects.all().values_list("username", flat=True))


def get_posts_list(
    search: str | None = None, username_search: str | None = None, tags: list[str] | None = None
):
    qs = (
        Post.objects.all()
        .select_related("owner")  # Это для foreign key связи
        .prefetch_related("tags")  # Это для many to many связи
        .only("id", "title", "image", "created_at", "updated_at", "owner__username")
    )

    if search:
        # Поиск по названию поста ИЛИ содержимому поста
        qs = qs.filter(Q(title__icontains=search) | Q(content__icontains=search))

    if username_search:
        qs = qs.filter(owner__username__iexact=username_search)

    if tags:
        qs = qs.filter(tags__name__in=tags).distinct()

    return qs


def add_tags_to_post(post: Post, tags: QuerySet[Tag], new_tags: list[str] | None = None) -> Post:
    """
    Добавляет теги к посту. Создает новые теги, если они не существуют.
    :param post: Существующая модель поста.
    :param tags: QuerySet тегов, которые нужно добавить к посту.
    :param new_tags: Список новых тегов, которые нужно создать и добавить к посту.
    """

    if tags:
        post.tags.set(tags)

    if new_tags is not None:
        for tag_name in new_tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)

    return post


def create_post(
    title: str,
    content: str,
    user: User,
    image: UploadedFile,
    tags: QuerySet[Tag],
    new_tags: list[str] | None = None,
) -> Post:

    post = Post.objects.create(title=title, content=content, owner=user, image=image)

    post = add_tags_to_post(post, tags, new_tags)
    return post


def update_post(
    post: Post,
    title: str,
    content: str,
    image: UploadedFile | None | bool,
    tags: QuerySet[Tag],
    new_tags: list[str] | None = None,
) -> Post:
    post.title = title
    post.content = content

    # Если False, то удаляем изображение
    # Если не None, то удаляем старое изображение
    if image is False or image is not None:
        if post.image is not None:
            post.image.delete(save=False)

    # Если image передан, то обновляем изображение
    if image:
        post.image = image

    post = add_tags_to_post(post, tags, new_tags)

    post.save(update_fields=["title", "content", "image", "updated_at"])
    return post


def create_comment(post: Post, user: User, content: str) -> Comment:
    return Comment.objects.create(text=content, owner=user, post=post)
