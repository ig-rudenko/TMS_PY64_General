import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests
from dotenv import load_dotenv

load_dotenv(".env.dev")


class APIError(Exception):
    pass


class AuthError(APIError):
    pass


class NotFoundError(APIError):
    pass


class DjangoPostsAPI:

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


def get_posts_with_threads(count: int = 10):
    posts_map: dict[int, list] = {}

    api = DjangoPostsAPI(token=os.getenv("API_TOKEN"), base_url=os.getenv("BASE_URL"))

    threads_count = 15
    print("Количество потоков:", threads_count)

    def get_posts(p: int):
        posts_map[p] = api.get_posts(page=p)["results"]

    start = time.perf_counter()

    # ==================================================================
    with ThreadPoolExecutor(max_workers=threads_count) as executor:
        for page in range(1, count + 1):
            executor.submit(get_posts, page)
    # ==================================================================

    print(f"Время получения {count} страниц:", round(time.perf_counter() - start, 4), "сек")

    posts = []
    for page in range(1, count):  # 4. Собираем результаты в один список в правильном порядке страниц.
        if page in posts_map:
            posts.extend(posts_map[page])

    print("Результаты:", len(posts))


if __name__ == "__main__":
    get_posts_with_threads(100)
