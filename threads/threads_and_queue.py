import os
import threading
import time
from queue import Queue

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


def worker(q: Queue[int], results: dict, api: DjangoPostsAPI):
    print(f"🤖 Запуск рабочего {threading.get_ident()} | процесс: {os.getpid()}")
    while True:
        if q.empty():
            break

        page = q.get_nowait()  # Получаем страницу из очереди
        posts = api.get_posts(page=page)
        results[page] = posts["results"]
        q.task_done()  # Удаляем страницу из очереди


def get_posts_with_threads(count: int = 10):
    posts_map: dict[int, list] = {}

    # ==============================================
    threads_count = 15
    print("Количество потоков:", threads_count)

    queue = Queue[int]()  # 0. Создаем очередь из страниц (только целые числа)
    for page in range(1, count):
        queue.put_nowait(page)
    # ==============================================

    api = DjangoPostsAPI(token=os.getenv("API_TOKEN"), base_url=os.getenv("BASE_URL"))

    worker_threads = []
    for i in range(1, threads_count):  # 1. Создаем потоки для рабочих функций
        worker_threads.append(
            threading.Thread(
                target=worker,
                args=(queue, posts_map, api),
                name=f"Worker {i}",
            )
        )

    start = time.perf_counter()
    for thread in worker_threads:  # 2. Запускаем все потоки рабочих функций
        thread.start()

    for thread in worker_threads:  # 3. Ждем завершения всех потоков рабочих функций
        thread.join()

    print(f"Время получения {count} страниц:", round(time.perf_counter() - start, 4), "сек")

    posts = []
    for page in range(1, count):  # 4. Собираем результаты в один список в правильном порядке страниц.
        if page in posts_map:
            posts.extend(posts_map[page])

    print("Результаты:", len(posts))


if __name__ == "__main__":
    get_posts_with_threads(100)
