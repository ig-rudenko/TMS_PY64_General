import os
import threading
import time

import requests
from dotenv import load_dotenv

load_dotenv(".env.dev")  # Загружаем переменные окружения из файла .env.dev


class APIError(Exception):
    """Базовое исключение для ошибок, связанных с API."""


class AuthError(APIError):
    """Исключение, возникающее при неудачной авторизации в API."""


class NotFoundError(APIError):
    """Исключение, возникающее при попытке получить несуществующий ресурс через API."""


class DjangoPostsAPI:
    """Клиент для взаимодействия с API блога на Django."""

    def __init__(self, token: str, base_url: str):
        self._token = token
        self._base_url = base_url
        self._headers = {
            "Authorization": f"Token {token}",
        }

    def get_posts(self, search: str = "", owner: str = "", page: int = 1) -> dict:
        prefix = f"Получение страницы: {page} | поток: {threading.get_ident()} | процесс: {os.getpid()}"
        print(prefix)

        start = time.perf_counter()
        resp = requests.get(
            f"{self._base_url}/api/v1/posts",
            params={
                "page": page,
                "search": search,
                "owner": owner,
            },
            headers=self._headers,
            timeout=5,
        )
        print(f"{prefix} | Времени затрачено {round(time.perf_counter() - start, 4)} сек")
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 401:
            raise AuthError(f"Authentication failed {resp.text}")
        if resp.status_code == 404:
            raise NotFoundError("Resource not found")
        raise APIError(f"API error {resp.status_code} {resp.text}")


def get_posts_no_threads(count: int = 10):
    """Получает посты без использования многопоточности."""
    posts = []
    api = DjangoPostsAPI(token=os.getenv("API_TOKEN"), base_url=os.getenv("BASE_URL"))

    start = time.perf_counter()
    for i in range(1, count):
        posts.extend(api.get_posts(page=i)["results"])
    print(f"Время получения {count} страниц:", round(time.perf_counter() - start, 4), "сек")


def get_posts_with_threads(count: int = 10):
    """Получает посты с использованием многопоточности."""
    posts_map: dict[int, list] = {}

    api = DjangoPostsAPI(token=os.getenv("API_TOKEN"), base_url=os.getenv("BASE_URL"))

    def get_posts(p: int):
        """Внутренняя функция для выполнения в отдельном потоке."""
        posts_map[p] = api.get_posts(page=p)["results"]

    threads = []
    for i in range(1, count):  # 1. Создаем потоки
        threads.append(
            threading.Thread(
                target=get_posts,
                args=(i,),
                name=f"Thread {i}",
            )
        )

    start = time.perf_counter()
    for thread in threads:  # 2. Запускаем все потоки
        thread.start()

    for thread in threads:  # 3. Ждем завершения всех потоков
        thread.join()
    print(f"Время получения {count} страниц:", round(time.perf_counter() - start, 4), "сек")

    posts = []
    for page in range(1, count):  # 4. Собираем результаты в один список в правильном порядке страниц.
        if page in posts_map:
            posts.extend(posts_map[page])

    print("Результаты:", len(posts))


def main():
    # get_posts_no_threads(30)
    get_posts_with_threads(100)


if __name__ == "__main__":
    main()
