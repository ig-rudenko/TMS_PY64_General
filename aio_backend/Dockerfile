FROM python:3.13.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 0. Создание рабочей директории и переход в неё.
WORKDIR /app

# 1. Копирование файла с зависимостями.
COPY requirements.txt .

# 2. Установка зависимостей.
RUN pip install -r requirements.txt --no-cache-dir

# 3. Копирование файлов проекта.
COPY . .
