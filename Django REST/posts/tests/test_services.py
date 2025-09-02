import shutil
from pathlib import Path

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from posts.models import Tag, Post
from posts.services import create_post

User = get_user_model()
MEDIA_ROOT = Path(__file__).parent / "media"


# @override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestCreatePostService(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@example.com"
        )
        cls.tag1 = Tag.objects.create(name="tag1")
        cls.tag2 = Tag.objects.create(name="tag2")
        cls.image_path = Path(__file__).parent / "cat_nice.png"

    def tearDown(self):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)

    def test_create_post_str_image(self):
        post = create_post(
            "Test Post",
            "Test Content",
            user=self.user,
            image="test_image.jpg",
            tags=Tag.objects.filter(name="tag1"),
            new_tags=["tag2"],
        )

        self.assertIsInstance(post, Post)

        self.assertEqual(post.image.name, "test_image.jpg", "Ошибка в имени изображения")
        self.assertEqual(Post.objects.count(), 1, "Пост не был создан")
        self.assertEqual(Tag.objects.count(), 2, "Ошибка в количестве тегов")
        self.assertEqual(post.tags.count(), 2, "Ошибка в количестве тегов у поста")

    def test_create_post_image(self):
        image_file = SimpleUploadedFile(
            name="cat_nice.png",
            content=self.image_path.read_bytes(),
            content_type="image/png",
        )

        with self.settings(MEDIA_ROOT=MEDIA_ROOT):
            post = create_post(
                "Test Post",
                "Test Content",
                user=self.user,
                image=image_file,
                tags=Tag.objects.filter(name="tag1"),
                new_tags=["tag2"],
            )

        self.assertIsInstance(post, Post)

        self.assertEqual(Post.objects.count(), 1, "Пост не был создан")
        self.assertEqual(Tag.objects.count(), 2, "Ошибка в количестве тегов")
        self.assertEqual(post.tags.count(), 2, "Ошибка в количестве тегов у поста")
