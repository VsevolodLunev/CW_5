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
клонировать репозиторий [Github] #1

Docker в проекте

Для быстрого старта:

Скачайте проект с удаленного репозитория

Настройте зависимости в файле .env

Введите в терминал команду: docker-compose up -d --build

1. Requirements
For a successful deployment you will need:
Remote server with Docker installed.
Docker Hub account.
Access to the repository on GitHub.
2. Setting up a remote server
System update:
sudo apt update
sudo apt upgrade
3. 
Installing docker and docker-compose:
sudo apt update && sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo usermod -aG docker $USER && newgrp docker

Firewall setup
Activate firewall
# check the firewall status
sudo ufw status

# If the firewall is disabled, enable it
sudo ufw enable

Open the necessary ports
# http port:
sudo ufw allow 80/tcp
	
# https port:
sudo ufw allow 443/tcp
	
# ssh port:
sudo ufw allow 22/tcp

Cloning a repository:
Fill in values. Here's an example:
git clone https://github.com/VsevolodLunev/CW_5/tree/feature1 /var/www/habit-tracker
cd /var/www/habit-tracker
Fill in values. Here's an example:
git clone https://github.com/VsevolodLunev/CW_5/tree/feature1 /var/www/habit-tracker
cd /var/www/habit-tracker
 