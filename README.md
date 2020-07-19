# Пульт охраны банка

Система учета, посещений хранилища банка по их идентификационным картам

### Как установить
Переименовать .env.example в .env, заполнить параметры

    SECRET_KEY - секретный ключ
    
    Настройка базы данных:
    DB_HOST
    DB_PORT
    DB_USER
    DB_PASSWORD
    
    Ркжим отладки:
    DEBUG=True
    
Устанавливаем зависимости
    
    pip install -r requirements.txt

Делаем миграцию БД

    python manager.py makemigrations
    python manager.py migrate

### Использование
для просмотра функционала, достаточно выполнить

    python manager.py runserver

открыть http://127.0.0.1:8000/

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).