from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.urls import reverse
from rest_framework.test import APITestCase

from posts.api.serializers import PostSerializer
from posts.models import Post, Tag
from posts.tests.factories import PostFactory, UserFactory

User = get_user_model()


class TestApiPostsList(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.posts = PostFactory.create_batch(10)
        cls.posts_list_url = reverse("api:posts-list-create")
        print(cls.posts)

    def tearDown(self):
        cache.clear()

    def test_get_posts(self):
        resp = self.client.get(self.posts_list_url)
        print(resp.data)
        self.assertEqual(len(resp.data["results"]), len(self.posts))

        self.assertNotIn("content", resp.data["results"][0], "Контент не должен быть в ответе")

    def test_get_posts_with_cache(self):
        with self.assertNumQueries(2):
            self.client.get(self.posts_list_url)

        with self.assertNumQueries(0):
            self.client.get(self.posts_list_url)

    def test_get_posts_no_cache_for_filters(self):
        post_owner = self.posts[0].owner
        with self.assertNumQueries(2):
            self.client.get(self.posts_list_url + f"?owner={post_owner.username}")

        with self.assertNumQueries(2):
            self.client.get(self.posts_list_url + f"?owner={post_owner.username}")

    def test_get_posts_no_cache_for_big_page_number(self):
        with self.assertNumQueries(1):
            self.client.get(self.posts_list_url + "?page=999999")

        with self.assertNumQueries(1):
            self.client.get(self.posts_list_url + "?page=999999")


class TestApiCreatePosts(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.create_post_url = reverse("api:posts-list-create")
        cls.user = UserFactory()

    def test_anon_create_post_no_auth(self):
        response = self.client.post(self.create_post_url)
        self.assertEqual(response.status_code, 401)

    def test_user_create_post(self):
        self.client.force_login(self.user)
        data = {
            "title": "test",
            "content": "test",
            "new_tags": ["tag1", "tag2"],
        }
        response = self.client.post(self.create_post_url, data)
        print(response.data)

        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Tag.objects.count(), 2)

        self.assertNotIn("content", response.data, "Контент не должен быть в ответе")
        serializer = PostSerializer(Post.objects.first())
        self.assertDictEqual(response.data, serializer.data)
