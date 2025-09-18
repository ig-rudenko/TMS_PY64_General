import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import aiofiles
import aiohttp
import requests

COUNT = 50
IMAGE_URL = "https://storage.yandexcloud.net/bookshelf/previews/14/preview.png"
EXTRA_PAUSE = 0


def download_file_thread(folder: Path) -> None:
    def _download_file(file_name: str):
        response = requests.get(IMAGE_URL)
        if response.status_code == 200:
            time.sleep(EXTRA_PAUSE)  # Simulate CPU bound
            with open(folder / file_name, "wb") as file:
                file.write(response.content)

    start = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        for i in range(COUNT):
            executor.submit(_download_file, f"image-{i}.png")
    print(f"THREADS | Download {COUNT} files in {time.perf_counter() - start:.2f} seconds")


async def download_file_async(folder: Path) -> None:

    async def _download_file(session: aiohttp.ClientSession, file_name: str):
        async with session.get(IMAGE_URL) as response:
            if response.status == 200:
                time.sleep(EXTRA_PAUSE)  # Simulate CPU bound
                async with aiofiles.open(folder / file_name, "wb") as file:
                    file_data = await response.read()
                    await file.write(file_data)

    async with aiohttp.ClientSession() as session:

        tasks = []
        for i in range(COUNT):
            tasks.append(
                asyncio.create_task(
                    _download_file(session, f"image-{i}.png"),
                )
            )

        start = time.perf_counter()
        await asyncio.gather(*tasks)
        print(f"ASYNC! | Download {COUNT} files in {time.perf_counter() - start:.2f} seconds")


if __name__ == "__main__":
    folder = Path("images")
    folder.mkdir(exist_ok=True)

    # download_file_thread(folder)
    asyncio.run(download_file_async(folder))


# CPU Bound = 0 sec per task:
# ASYNC! | Download 50 files in 1.89 seconds

# CPU Bound = 0.1 sec per task:
# ASYNC! | Download 50 files in 5.67 seconds

# CPU Bound = 0.2 sec per task:
# ASYNC! | Download 50 files in 10.68 seconds
