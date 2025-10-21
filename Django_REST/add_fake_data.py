import os
import random

from django import setup
from django.db.transaction import atomic
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
setup()

# --------------------------------------------------------------------------------------------------------------------

from accounting.models import User
from posts.models import Post, Tag, Comment


USERS_COUNT = 100
TAGS_COUNT = 200
POSTS_PER_USER = 1000
COMMENTS_PER_POST = 10


def create_users(faker: Faker) -> list[User]:
    users = []
    for i in range(USERS_COUNT):
        users.append(
            User(
                username=faker.unique.user_name(),
                email=faker.unique.email(),
                password=faker.password(length=12),
                first_name=faker.first_name(),
                last_name=faker.last_name(),
            )
        )
    users = User.objects.bulk_create(users)
    for user in users:
        user.set_password(user.password)

    User.objects.bulk_update(users, ["password"])
    return users


def create_tags(faker: Faker) -> list[Tag]:
    tags = []
    for i in range(TAGS_COUNT):
        tags.append(Tag(name=faker.unique.word()))
    return Tag.objects.bulk_create(tags)


def create_posts(faker: Faker, user: User, tags_list: list[Tag]) -> list[Post]:
    posts = []
    for i in range(POSTS_PER_USER):
        posts.append(Post(title=faker.sentence(), content=faker.text(), owner=user))
    posts = Post.objects.bulk_create(posts)

    posts_tags_model = Post.tags.through
    posts_tags = []
    for post in posts:
        tags = random.sample(tags_list, random.randint(3, 5))
        for tag in tags:
            posts_tags.append(posts_tags_model(post_id=post.id, tag_id=tag.name))
    posts_tags_model.objects.bulk_create(posts_tags)
    return posts


def create_comment(faker: Faker, post: Post, user: User) -> list[Comment]:
    comments = []
    for i in range(COMMENTS_PER_POST):
        comments.append(Comment(text=faker.text(), post=post, owner=user))
    return Comment.objects.bulk_create(comments)


def main():
    faker = Faker("ru_RU")

    with atomic():
        users = create_users(faker)
        print("Users created:", USERS_COUNT)

        tags_list = create_tags(faker)
        print("Tags created:", TAGS_COUNT)

        posts = []
        for user in users:
            posts.extend(create_posts(faker, user, tags_list))
            print(f"Posts created: for user {user.username}")

        for i, post in enumerate(posts):
            create_comment(faker, post, random.choice(users))
            print("Осталось", len(posts) - i, "постов")


if __name__ == "__main__":
    main()
