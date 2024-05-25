# To-Do List Application

## Описание

Это небольшое веб-приложение на Flask, которое предоставляет RESTful API для управления списком задач (To-Do list). 
Приложение включает в себя следующие возможности:

1. Создание задачи
2. Получение списка задач
3. Получение информации о задаче
4. Обновление задачи
5. Удаление задачи



## Установка

### Требования

- Python 3.12
- Poetry (для управления зависимостями)

### Шаги установки

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/todo_app.git
   cd todo_app

    Установите зависимости:

    bash

poetry install

Создайте базу данных MySQL:

sql

CREATE DATABASE todo_app;

Настройте переменные окружения:

Создайте файл .env в корневой директории проекта и добавьте следующие переменные:

env

SECRET_KEY=your_secret_key
DATABASE_URL=mysql+mysqlconnector://username:password@localhost/todo_app

Инициализируйте базу данных:

bash

    poetry run flask db init
    poetry run flask db migrate -m "Initial migration."
    poetry run flask db upgrade

Запуск

Для запуска приложения используйте следующую команду:

bash

poetry run python run.py

Приложение будет доступно по адресу http://127.0.0.1:5000.
API Эндпоинты
Создание задачи

    Метод: POST
    URL: /api/tasks
    Параметры запроса: JSON-объект с полями title (строка) и description (строка, опционально).
    Ответ: JSON-объект с полями id, title, description, created_at, updated_at.

Получение списка задач

    Метод: GET
    URL: /api/tasks
    Ответ: JSON-список задач, где каждая задача представляет собой JSON-объект с полями id, title, description, created_at, updated_at.

Получение информации о задаче

    Метод: GET
    URL: /api/tasks/<id>
    Ответ: JSON-объект с полями id, title, description, created_at, updated_at.

Обновление задачи

    Метод: PUT
    URL: /api/tasks/<id>
    Параметры запроса: JSON-объект с полями title (строка, опционально) и description (строка, опционально).
    Ответ: JSON-объект с полями id, title, description, created_at, updated_at.

Удаление задачи

    Метод: DELETE
    URL: /api/tasks/<id>
    Ответ: Сообщение об успешном удалении.

Тестирование

Для запуска тестов используйте следующую команду:

bash

poetry run pytest


```
Flask
Flask-SQLAlchemy
Flask-Migrate
mysql-connector-python
Flask-RESTful


```