# restaurant_menu_application

## Описание

REST API сервис для отображения меню ресторана.

## Технологии

Python 3.9
Django 4.2.14
Django REST framework 3.15.2

## Запуск проекта в режиме разработки

Клонируем репозиторий и переходим в него в командной строке:

```bash
git clone https://github.com/afanasev-ilia/restaurant_menu_application.git
```

```bash
cd restaurant_menu_application
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

```bash
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python manage.py migrate
```

Запустить проект:

```bash
python manage.py runserver
```

Запустить тесты для views.py:

```bash
python manage.py test
```

## Шаблон наполнения .env
```
SECRET_KEY='********************************'
```

## Автор
Илья Афанасьев