import time
from math import factorial

import asyncio


async def calc():
    res = []  # CPU bound
    for i in range(3000):  # CPU bound
        f = factorial(i)  # CPU bound
        res.append(f)  # CPU bound
    return res  # CPU bound


async def main():
    start = time.perf_counter()
    tasks = []
    for i in range(10):
        tasks.append(
            asyncio.create_task(calc()),
        )

    results = await asyncio.gather(*tasks)
    print(f"Finished in {time.perf_counter() - start} seconds")
    print(len(results))


if __name__ == "__main__":
    asyncio.run(main())
