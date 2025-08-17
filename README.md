# 🗒️ Django Notes ORM

## 📖 Описание проекта
**Django Notes ORM** — это учебное веб-приложение на Django с использованием PostgreSQL и Docker.  
Проект демонстрирует:
- работу с **Django ORM** (без raw SQL),
- подключение **шаблонов Django**,
- оптимизацию запросов (`select_related`, `prefetch_related`),
- стилизацию интерфейса с помощью **Bootstrap**.

Приложение позволяет просматривать список заметок, детальные страницы заметок, пользователей и их записи.

---

## 🚀 Функционал

### 1. Главная страница `/`
- Список всех заметок:
  - текст (до 100 символов),
  - автор,
  - статус,
  - категории,
  - дата создания.
- Запросы оптимизированы с помощью `select_related` и `prefetch_related`.

### 2. Детальная страница заметки `/notes/<id>/`
- Полный текст заметки.
- Автор (имя, email, биография, дата рождения).
- Статус и отметка «финальный».
- Список категорий.

### 3. Страница пользователя `/users/<id>/`
- Имя пользователя, email, биография, дата рождения.
- Список всех его заметок с текстом и статусом.

### 4. Список пользователей `/users/`
- Навигация по всем пользователям (отсортированы по имени).

---

## 🛠 Технологии
- **Python 3.11**
- **Django 4.x**
- **PostgreSQL 16**
- **Docker + Docker Compose**
- **Bootstrap 5**
- **Faker** (генерация тестовых данных)

---

## 📂 Структура проекта
```

django-notes-orm-Andasbek/
│── notes/                 # Основное Django-приложение
│   ├── models.py          # Модели User, UserProfile, Note, Status, Category
│   ├── views.py           # Логика отображения страниц
│   ├── urls.py            # Маршрутизация приложения
│   ├── templates/notes/   # HTML-шаблоны
│   └── tests.py           # Тесты
│
│── static/                # Статические файлы
│── seed.py                 # Скрипт заполнения БД тестовыми данными
│── docker-compose.yml      # Запуск через Docker
│── Dockerfile              # Образ приложения
│── .env                    # Настройки окружения
│── manage.py

````

---

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone <repo_url>
cd django-notes-orm-Andasbek
````

### 2. Создать файл `.env`

```env
POSTGRES_DB=notes_db
POSTGRES_USER=notes_user
POSTGRES_PASSWORD=notes_pass
POSTGRES_HOST=db
POSTGRES_PORT=5432
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin
LANGUAGE_CODE=ru
TIME_ZONE=Asia/Almaty
```

### 3. Запустить проект

```bash
docker compose up --build
```

### 4. Применить миграции и заполнить данными

```bash
docker compose exec web python manage.py migrate
docker compose exec web python seed.py
```

---

## 🔗 Основные страницы

| Страница              | URL            | Описание                      |
| --------------------- | -------------- | ----------------------------- |
| Главная               | `/`            | Все заметки                   |
| Детальная заметка     | `/notes/<id>/` | Информация о заметке          |
| Список пользователей  | `/users/`      | Список всех пользователей     |
| Страница пользователя | `/users/<id>/` | Данные и заметки пользователя |
| Админ-панель          | `/admin/`      | Управление проектом           |

---

## 🧪 Тестирование

```bash
docker compose exec web python manage.py test -v 2
```

---

## 📌 Особенности

* Количество тестовых заметок ограничено **10**.
* Все данные генерируются с помощью **Faker**.
* Локализация интерфейса (RU).
* Чистый код и оптимизированные запросы.

