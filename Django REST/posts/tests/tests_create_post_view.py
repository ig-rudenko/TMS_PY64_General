from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse

from posts.models import Post, Tag

User = get_user_model()


class CreatePostViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Метод вызывается один раз перед всеми тестами в классе.
        """
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword", email="testemail@test.com"
        )
        cls.create_url = reverse("post-create")
        cls.login_url = reverse("login")

    def setUp(self):
        """
        Этот метод вызывается перед каждым тестом.
        """

    def tearDown(self):
        """
        Этот метод вызывается после каждого теста.
        """
        cache.clear()

    def test_anon_create_post_view(self):
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url + "?next=" + self.create_url)

    def test_user_create_post_view(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("post-create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/create.html")

    def test_user_create_post_view_post(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("post-create"),
            {
                "title": "test title",
                "content": "test content",
                "new_tags": "tag1, tag2",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Tag.objects.count(), 2)

    def test_user_create_post_view_empty_title_data(self):
        self.client.force_login(self.user)

        self.client.post(
            reverse("post-create"),
            {
                "title": "",
                "content": "test content",
                "new_tags": "tag1, tag2",
            },
        )

        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(Tag.objects.count(), 0)

    def test_user_create_post_view_short_title_data(self):
        self.client.force_login(self.user)
        self.client.post(
            reverse("post-create"),
            {
                "title": "1",
                "content": "test content",
                "new_tags": "tag1, tag2",
            },
        )

        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(Tag.objects.count(), 0)

    def test_user_create_post_view_empty_content_data(self):
        self.client.force_login(self.user)

        self.client.post(
            reverse("post-create"),
            {
                "title": "title",
                "content": "",
                "new_tags": "tag1, tag2",
            },
        )

        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(Tag.objects.count(), 0)

    def test_user_create_post_view_invalid_tags_data(self):
        self.client.force_login(self.user)

        self.client.post(
            reverse("post-create"),
            {
                "title": "title",
                "content": "",
                "tags": [1, 2],
                "new_tags": "tag1, tag2",
            },
        )

        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(Tag.objects.count(), 0)

    def test_user_create_post_view_with_exists_tags_data(self):
        """
        Проверка, что при создании поста с уже существующими тегами, они не будут созданы повторно
        """
        self.client.force_login(self.user)

        tag1 = Tag.objects.create(name="tag1")
        tag2 = Tag.objects.create(name="tag2")

        self.client.post(
            reverse("post-create"),
            {
                "title": "title",
                "content": "content",
                "tags": [tag1.name, tag2.name],
                "new_tags": f"{tag1.name}, {tag2.name}, tag3",
            },
        )

        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Tag.objects.count(), 3)
