приложение на Django REST
Приложение habits с различными привычками
Приложение имеет следующий функционал:
Пользователь — создатель привычки.
Место — место, в котором необходимо выполнять привычку.
Время — время, когда необходимо выполнять привычку.
Действие — действие, которое представляет собой привычка.
Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.

Установка
клонировать репозиторий [[Github](https://github.com/VsevolodLunev/CW_5/tree/feature3)] #1

🛠 Технологии
Python 3.13
Django 5.2.5
PostgreSQL
Redis
Celery
Nginx
Docker + Docker Compose
GitHub Actions (CI/CD)

🚀 Запуск проекта
Локальная разработка (с Docker)
Склонируйте репозиторий:
git clone git@github.com:VsevolodLunev/CW_5.git

Создайте файл .env в корне проекта (пример в .env.example):

 SECRET_KEY=<ваш-secret-key>
 POSTGRES_DB=<имя-бд>
 POSTGRES_USER=<пользователь-бд>
 POSTGRES_PASSWORD=<пароль-бд>
 # Остальные переменные...

Запустите сервисы:
docker-compose up -d

Примените миграции:
docker-compose exec web python manage.py migrate

Создайте суперпользователя (опционально):
docker-compose exec web python manage.py migrate

Проект доступен по адресу:
http://localhost:8000

☁️ Деплой на сервер
Требования к серверу
Ubuntu 22.04 LTS

Установка Docker и Docker Compose

Инструкция по настройке сервера
Установите Docker:
sudo apt-get update && sudo apt-get install docker.io docker-compose-plugin

Установите фаервол:
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
sudo ufw enable

Добавьте пользователя в группу docker:
sudo usermod -aG docker $USER

Настройка CI/CD
Добавьте secrets в GitHub (Settings → Secrets and variables → Actions):

DOCKER_HUB_USERNAME — логин Docker Hub

DOCKER_HUB_TOKEN — токен доступа

SSH_KEY — приватный SSH-ключ для доступа к серверу

SSH_USER — пользователь сервера (обычно root или ubuntu)

SERVER_IP — IP сервера 

DJANGO_SECRET_KEY - секретный ключ Django

TELEGRAM_BOT_TOKEN - токен Telegram-бота

Workflow автоматически выполнит:
Тестирование и линтинг
Сборку Docker-образов
Деплой на сервер при пуше