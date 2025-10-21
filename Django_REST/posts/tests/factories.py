import factory
from factory.django import DjangoModelFactory

from accounting.models import User
from posts.models import Tag, Post


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Sequence(lambda n: f"tag{n}")


class PostSimpleFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=4)
    content = factory.Faker("paragraph", nb_sentences=30)
    image = factory.Faker("url")


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password")


class PostFactory(PostSimpleFactory):
    owner = factory.SubFactory(UserFactory)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tag_kwargs in extracted:
                tag = TagFactory(**tag_kwargs)
                self.tags.add(tag)
        else:
            tags = TagFactory.create_batch(3)
            self.tags.set(tags)
