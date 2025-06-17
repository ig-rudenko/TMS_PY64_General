# Первыми импортируются встроенные библиотеки/модули.
import random
import math
from time import sleep as time_sleep, perf_counter


def sleep(seconds: int):
    print(f"Я буду спать {seconds} секунд")
    time_sleep(seconds)

# Затем импортируются сторонние библиотеки/модули. (Которые нужно предварительно скачать)
# import requests

# И только после этого импортируются модули из текущего проекта (Написанные программистами вашей команды или вами).
# import str_formats  # В момент импорта модуля он будет выполнен полностью!

# Напишите в коде случайное число от 1 до 100.

start_time = perf_counter()
print(2 ** 0.5)
print("Пауза на 1 секунду")
sleep(1)
print("Прошла 1 секунда")

end_time = perf_counter()
print("Программа выполнилась за:", end_time - start_time, "секунд")
