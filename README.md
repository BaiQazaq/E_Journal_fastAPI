# Электронный Журнал для Оценок

## Описание

Это упрощенная версия электронного журнала для управления оценками учеников. Приложение предоставляет API для выполнения CRUD операций с учениками и их оценками.

## Технологический стек

- **FastAPI**: Используется для создания API эндпоинтов.
- **SQLAlchemy**: Используется для взаимодействия с базой данных.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository

2. Создайте виртуальное окружение и активируйте его:
   
    python3 -m venv venv
    source venv/bin/activate  # Для Linux/MacOS
    .\venv\Scripts\activate  # Для Windows

3. Установите зависимости:
   
    pip install -r requirements.txt

4. Запустите приложение:

    uvicorn main:app --reload

Использование
После запуска приложения API будет доступен по адресу http://127.0.0.1:8000.


Структура проекта
```
.
├── __pycache__
├── api
│   ├── __init__.py
│   ├── __pycache__
│   ├── scores
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── score_crud.py
│   │   ├── score_schemas.py
│   │   └── score_views.py
│   └── students
│       ├── __init__.py
│       ├── __pycache__
│       ├── students_crud.py
│       ├── students_schemas.py
│       └── students_view.py
├── core
│   ├── __init__.py
│   ├── __pycache__
│   ├── models
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── database.py
│   │   └── models.py
│   └── settings.py
├── main.py
├── requirements.txt
├── test.db
└── venv
```

* api/__init__.py: Инициализационный файл для пакета api.
* api/scores/score_crud.py: Функции CRUD для работы с оценками.
* api/scores/score_schemas.py: Pydantic схемы для оценок.
* api/scores/score_views.py: Эндпоинты для оценок.
* api/students/students_crud.py: Функции CRUD для работы с учениками.
* api/students/students_schemas.py: Pydantic схемы для учеников.
* api/students/students_view.py: Эндпоинты для учеников.
* core/models/database.py: Настройка базы данных.
* core/models/models.py: Определение моделей SQLAlchemy.
* core/settings.py: Настройки проекта.
* main.py: Основной файл приложения.
