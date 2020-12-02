![Foodgram](https://github.com/frolkit/foodgram-project/workflows/Foodgram/badge.svg)

# [Foodgram Project](https://foodgram.frolkit.ru/)
Это дипломный проект в Yandex Praktikum. Сайт, на котором пользователи могут оставлять свои рецепты, подписываться на авторов, ставить лайки и формировать список покупок на основе выбранных рецептов. Красивый и интерактивный сайт.

Стек: Django, Python, Docker, PostgreSQL, Nginx, GitHub Actions.

Сайт доступен: https://foodgram.frolkit.ru/

## Инструкция по развёртыванию.
1. Создайте отдельную папку для проекта. Все дальнейшие действия выполняйте из неё.

2. Скопируйте себе файл docker-compose.yaml

3. Создайте и заполните файл .env
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

4. Запустите контейнеры
```
docker-compose up -d
```

5. Сделайте миграции.
```
docker-compose exec web python manage.py migrate
```

6. Сервер доступен по 127.0.0.1:80

## Настройка приложения.

1. Создание суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```

2. Заполнение базы данных вводными данными
```
docker-compose exec web python manage.py loaddata < fixtures.json
```

