# Бот заметка

Ссылка на бота - https://t.me/aiogram_note_bot

## Про бота

Помогает писать заметки и потом их удобно менеджить.

Бот написан на aiogram + orm


## Инструкция по установке

**Должен быть установлен python**

*для linux вместо python -> python3.X, где 3.X - версия python*

#### 1)Клонируем репозиторий

    git clone https://github.com/Badsnus/YANDEX_INTENSIV.git

#### 2)Создаем виртуальное окружение и активируем его

    python -m venv venv

    Windows: venv\Scripts\activate.bat
    Linux и MacOS: source venv/bin/activate
    
#### 3)Заходим в директорию репозитория

    cd YANDEX_INTENSIV

#### 4) Устанавливаем зависимости

    pip install -r requirements.txt

#### 5)Заходим в директорию джанго проекта

    cd YANDEX_INTENSIV

#### 6) .env_example -> .env

    В YANDEX_INTENSIV есть файл .env_example его нужно переименовать в .env 

#### 7) Запускам проект

    python manage.py runserver
