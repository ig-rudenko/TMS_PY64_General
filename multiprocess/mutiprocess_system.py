import multiprocessing as mp
import os
import random
import time


def logger(log_queue: mp.Queue):
    try:
        with open("log.txt", "w", encoding="utf-8") as f:
            f.write(f"✅ Starting logger process | PID: {os.getpid()}\n")
            while True:
                text = log_queue.get()
                print(text)
                f.write(text + "\n")
    except KeyboardInterrupt:
        pass


def worker_spawner(work_queue: mp.Queue, log_queue: mp.Queue, semaphore: mp.Semaphore):
    try:
        log_queue.put(f"✅ Starting worker spawner process | PID: {os.getpid()}")
        worker_num = 1
        while True:
            semaphore.acquire()  # Занимаем семафор, пока не освободится
            worker_process = mp.Process(target=worker, args=(work_queue, log_queue, worker_num, semaphore))
            worker_process.start()
            worker_num += 1
    except KeyboardInterrupt:
        try:
            log_queue.put(f"Worker spawner interrupted | PID: {os.getpid()}")
        except:
            pass


def worker(work_queue: mp.Queue, log_queue: mp.Queue, worker_num: int, semaphore: mp.Semaphore):
    try:
        log_queue.put(f"✅ Starting worker-{worker_num} process | PID: {os.getpid()}")
        while True:
            data = work_queue.get()
            log_queue.put(f"Worker-{worker_num} received data: {data}")

            simulate_data(data)

    except KeyboardInterrupt:  # Если процесс получил сигнал о завершении работы
        try:
            log_queue.put(f"Worker-{worker_num} interrupted | PID: {os.getpid()}")
        except:
            pass

    finally:  # В любом случае освобождаем семафор
        try:
            semaphore.release()  # Освобождаем семафор
            log_queue.put(f"Worker-{worker_num} finished | PID: {os.getpid()}")
        except:
            pass


# ===================== Simulate some processing =====================


def simulate_data(number: int):
    time.sleep(1)
    if number < 10:  # 10% chance of error
        raise ValueError("ERROR OCCURED!")


def generator(work_queue: mp.Queue):
    try:
        while True:
            work_queue.put(random.randint(0, 100))
            time.sleep(random.random() * 2)
    except KeyboardInterrupt:
        pass


# =====================================================================


def main():
    print("✅ Starting main process")

    manager = mp.Manager()  # Создаем менеджер процессов

    work_queue = manager.Queue()
    log_queue = manager.Queue()
    semaphore = mp.Semaphore(3)  # Создаем семафор с 3 разрешениями

    generator_process = mp.Process(target=generator, args=(work_queue,))
    generator_process.start()

    worker_spawner_process = mp.Process(target=worker_spawner, args=(work_queue, log_queue, semaphore))
    worker_spawner_process.start()

    logger_process = mp.Process(target=logger, args=(log_queue,))
    logger_process.start()

    try:
        generator_process.join()
        worker_spawner_process.join()
        logger_process.join()
    except KeyboardInterrupt:  # Если пользователь прерывает работу основного процесса
        generator_process.terminate()
        generator_process.join()
        worker_spawner_process.terminate()
        worker_spawner_process.join()
        logger_process.terminate()
        logger_process.join()

    print("✅ All processes finished")


if __name__ == "__main__":
    main()
