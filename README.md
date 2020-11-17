![Foodgram](https://github.com/frolkit/foodgram-project/workflows/Foodgram/badge.svg)

# [Foodgram Project](https://foodgram.frolkit.gq/)
Это дипломный проект в Yandex Praktikum. Сайт, на котором пользователи могут оставлять свои рецепты, подписываться на авторов, ставить лайки и формировать список покупок на основе выбранных рецептов. Красивый и интерактивный сайт.

Стек: Django, Python, Docker, PostgreSQL, Nginx, GitHub Actions.

Сайт доступен: https://foodgram.frolkit.gq/

## Инструкция по развёртыванию.

1. Скопируйте себе файл docker-compose.yaml

2. Создайте и заполните файл .env
```
DEBUG=False
SECRET_KEY=Сгенерируйте ключ
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgresql
POSTGRES_USER=postgresql
POSTGRES_PASSWORD=postgresql
DB_HOST=db
DB_PORT=5432
```

3. Запустите контейнеры
```
docker-compose up -d
```

4. Сервер доступен по http//:127.0.0.1

## Настройка приложения.

Настройка https

Настройка домена

Создание суперпользователя

Заполнение базы данных вводными данными

Приложение готово
