from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import UploadedFile
from django.db.models import Q

from posts.models import Post, Comment

User = get_user_model()  # Возвращает модель пользователя текущего проекта.


def get_posts_list(search: str | None = None):
    qs = Post.objects.all()
    if search:
        # Поиск по названию поста ИЛИ содержимому поста
        qs = qs.filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        )

    return qs


def create_post(title: str, content: str, user: User, image: UploadedFile) -> Post:
    return Post.objects.create(title=title, content=content, owner=user, image=image)


def update_post(post: Post, title: str, content: str, image: UploadedFile | None | bool) -> Post:
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

    post.save()
    return post


def create_comment(post: Post, user: User, content: str) -> Comment:
    return Comment.objects.create(text=content, owner=user, post=post)
