from datetime import datetime

from django.core.cache import cache
from django.core.files.storage import default_storage
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.services import create_post
from .filters import PostFilter, CommentFilter
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    PostSerializer,
    CommentSerializer,
    PostWithViewsCountSerializer,
    ImageUploadSerializer,
)
from .throttling import CommentThrottle
from ..models import Post, Comment


class PostListCreateAPIView(ListCreateAPIView):
    """
    Представление для получения списка постов и создания нового поста.
    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().select_related("owner")  # Набор всех постов с предзагрузкой владельца.
    filter_backends = (filters.DjangoFilterBackend,)  # Используется фильтрация по параметрам.
    filterset_class = PostFilter  # Класс фильтрации для постов.
    cache_key = "posts_list"
    version_cache_key = "posts_list_version"
    cache_timeout = 60 * 15
    max_page_cached = 10  # Количество страниц, которые можно кешировать

    def can_use_cache(self) -> bool:
        """
        Проверяет, возможно ли использование кэша для текущего запроса.
        """
        page: str = self.request.GET.get("page", "")
        params = set(self.request.GET.keys())
        params.discard("page")

        if len(params) > 0 or (page.isdigit() and int(page) > self.max_page_cached):
            return False
        return True

    def get_cache_key(self) -> str:
        """
        Генерирует ключ кэша для текущей страницы.
        """
        page: str = self.request.GET.get("page", "")
        if page.isdigit():
            return f"{self.cache_key}:page:{int(page)}"
        return self.cache_key

    def get_cache_version(self) -> int:
        """
        Получает текущую версию кэша.

        Returns:
            int: Текущая версия кэша.
        """
        version = cache.get(self.version_cache_key, default=0)
        try:
            return max(int(version), 0)
        except ValueError:
            return 0

    def increment_cache_version(self):
        """
        Увеличивает версию кэша на единицу.
        """
        try:
            cache.incr(self.version_cache_key, delta=1)
        except ValueError:
            cache.set(self.version_cache_key, 0)

    def get(self, request, *args, **kwargs):
        """
        Обрабатывает GET-запрос. Если кэш доступен — возвращает его данные, иначе формирует и сохраняет в кэш.
        """
        if not self.can_use_cache():
            return super().get(request, *args, **kwargs)

        cache_version = self.get_cache_version()
        cache_key = self.get_cache_key()
        cache_data = cache.get(cache_key, version=cache_version)
        if cache_data is None:
            print("CACHE IS EMPTY")
            cache_data = super().get(request, *args, **kwargs).data
            cache.set(cache_key, cache_data, self.cache_timeout, version=cache_version)

        return Response(cache_data)

    def perform_create(self, serializer):
        """
        Выполняет создание нового поста, используя сервис `create_post`.

        Args:
            serializer (PostSerializer): Сериализатор с валидированными данными.
        """
        print("self.request.data =", self.request.data)
        print("type(self.request.data) =", type(self.request.data))
        print("serializer.validated_data", serializer.validated_data)
        serializer.instance = create_post(
            title=serializer.validated_data["title"],
            content=serializer.validated_data["content"],
            user=self.request.user,
            image=serializer.validated_data.get("image"),
            new_tags=serializer.validated_data["new_tags"],
        )
        self.increment_cache_version()


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления конкретного поста.
    """

    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = "id"  # Поле для поиска поста (id).
    lookup_url_kwarg = "id"  # Имя параметра URL для передачи id.
    cache_views_key = "post_views_count"  # Ключ кэша для подсчёта просмотров поста.

    def get_cache_key(self) -> str:
        """
        Генерирует ключ кэша для подсчёта просмотров конкретного поста.
        """
        return f"{self.cache_views_key}:{self.kwargs['id']}"

    @staticmethod
    def get_seconds_to_midnight() -> int:
        """
        Вычисляет количество секунд до полуночи текущего дня.
        """
        now = datetime.now()
        return int(
            datetime(year=now.year, month=now.month, day=now.day, hour=23, minute=59, second=59).timestamp()
            - now.timestamp()
        )

    def increment_views(self):
        """
        Увеличивает счётчик просмотров поста в кэше.
        """
        try:
            cache.incr(key=self.get_cache_key(), delta=1)
        except ValueError:
            cache.set(key=self.get_cache_key(), value=1, timeout=self.get_seconds_to_midnight())

    def get(self, request, *args, **kwargs):
        """
        Обрабатывает GET-запрос, увеличивает счётчик просмотров поста.
        """
        self.increment_views()
        resp = super().get(request, *args, **kwargs)
        return resp

    def get_serializer_class(self):
        """
        Возвращает соответствующий сериализатор в зависимости от HTTP-метода.
        """
        if self.request.method == "GET":
            return PostWithViewsCountSerializer
        return PostSerializer


class CommentListCreateAPIView(ListCreateAPIView):
    """
    Представление для получения списка комментариев и создания нового комментария.
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all().select_related("owner")
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CommentFilter

    def get_throttles(self):
        if self.request.method == "POST":
            return [CommentThrottle()]
        return []

    def perform_create(self, serializer):
        """
        Создаёт новый комментарий и привязывает его к текущему пользователю.

        Args:
            serializer (CommentSerializer): Сериализатор с валидированными данными.
        """
        serializer.save(owner=self.request.user)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления конкретного комментария.
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = "id"
    lookup_url_kwarg = "id"


class ImageUploadAPIView(APIView):
    """
    Представление для загрузки изображения.
    """

    serializer_class = ImageUploadSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Обрабатывает POST-запрос, загружает изображение и сохраняет его в хранилище.
        """
        # Инициализируем сериализатор данными из запроса (изображение)
        serializer = self.serializer_class(data=request.data)

        # Проверяем валидность данных. Если данные не валидны — выбрасывается исключение
        serializer.is_valid(raise_exception=True)

        # Получаем объект изображения из проверенных данных
        image = serializer.validated_data["image"]

        now = datetime.now()
        # Формируем путь, куда будет сохранено изображение: год/месяц/день/имя_файла
        # Например: 2025/4/5/example.jpg
        # `default_storage` — это объект хранилища файлов Django по умолчанию.
        # Метод `save()` сохраняет файл по указанному пути и возвращает его относительный путь.
        image_path = default_storage.save(f"{now.year}/{now.month}/{now.day}/{image.name}", image)

        # Возвращаем ответ с путём сохранённого изображения и статусом 201 Created
        return Response({"image_path": image_path}, status=status.HTTP_201_CREATED)
