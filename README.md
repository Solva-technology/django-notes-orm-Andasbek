# 🗒️ Django Notes ORM

## 📖 Описание проекта

**Django Notes ORM** — учебное веб-приложение для управления заметками, демонстрирующее:
- Работу с **Django ORM** и оптимизацию запросов
- Связи между моделями (ForeignKey, ManyToMany, OneToOne)
- Использование `select_related` и `prefetch_related` для предотвращения N+1 проблемы
- Шаблонную систему Django с наследованием
- Контейнеризацию через Docker
- Стилизацию интерфейса с **Bootstrap 5**

---

## 🚀 Функционал

### Заметки
- **Список заметок** (`/`) — все заметки с пагинацией, автором, статусом, категориями
- **Детальная страница** (`/<id>/`) — полный текст, профиль автора, категории
- **Создание** (`/create/`) — форма создания новой заметки
- **Редактирование** (`/<id>/edit/`) — изменение существующей заметки

### Пользователи
- **Список пользователей** (`/users/`) — все пользователи с сортировкой по имени
- **Профиль пользователя** (`/users/<id>/`) — информация, биография, заметки пользователя

### Категории
- **Список категорий** (`/categories/`) — все категории с количеством заметок
- **Заметки по категории** (`/categories/<id>/`) — фильтрация заметок

### Администрирование
- **Админ-панель** (`/admin/`) — управление всеми сущностями

---

## 🛠 Технологии

- **Python 3.11**
- **Django 5.2.7**
- **PostgreSQL 16**
- **Docker + Docker Compose**
- **Bootstrap 5.3**
- **Faker** для генерации тестовых данных

---

## 📂 Структура проекта

```
django-notes-orm-Andasbek/
├── notes/                      # Основное приложение заметок
│   ├── models.py               # User, UserProfile, Note, Status, Category
│   ├── views.py                # Контроллеры для обработки запросов
│   ├── urls.py                 # URL-маршруты
│   ├── forms.py                # Формы Django
│   ├── admin.py                # Настройка админ-панели
│   └── templates/notes/        # Шаблоны заметок
├── users/                      # Приложение пользователей
│   ├── views.py                # Контроллеры для пользователей
│   ├── urls.py                 # URL-маршруты пользователей
│   └── templates/users/        # Шаблоны профилей
├── templates/                  # Глобальные шаблоны
│   ├── base.html               # Базовый шаблон
│   └── includes/               # Header, footer
├── static/                     # Статические файлы (CSS, JS, изображения)
├── notebook_project/           # Настройки проекта
│   ├── settings.py
│   └── urls.py
├── seed.py                     # Скрипт генерации тестовых данных
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env                        # Переменные окружения (не в git!)
└── manage.py
```

---

## ⚙️ Установка и запуск

### Требования
- Docker Desktop
- Git

### 1. Клонировать репозиторий

```bash
git clone <repo_url>
cd django-notes-orm-Andasbek
```

### 2. Создать файл `.env`

```bash
cat > .env << 'EOF'
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
EOF
```

### 3. Запустить проект

```bash
# Собрать и запустить контейнеры
docker compose up --build -d

# Применить миграции
docker compose exec web python manage.py migrate

# Создать суперпользователя (автоматически из .env)
docker compose exec web python manage.py createsuperuser --noinput

# Заполнить БД тестовыми данными
docker compose exec web python seed.py
```

### 4. Открыть приложение

Проект доступен по адресу: **http://localhost:8000**

---

## 🔗 Основные URL

| Страница | URL | Описание |
|----------|-----|----------|
| Главная | `/` | Список всех заметок |
| Создание заметки | `/create/` | Форма создания |
| Детальная заметка | `/<id>/` | Полная информация о заметке |
| Редактирование | `/<id>/edit/` | Изменение заметки |
| Список пользователей | `/users/` | Все пользователи |
| Профиль пользователя | `/users/<id>/` | Информация и заметки |
| Список категорий | `/categories/` | Все категории |
| Заметки категории | `/categories/<id>/` | Фильтр по категории |
| Админ-панель | `/admin/` | Управление данными |

**Вход в админку:** admin / admin

---

## 🐳 Управление Docker

### Основные команды

```bash
# Запустить контейнеры
docker compose up -d

# Остановить контейнеры
docker compose stop

# Перезапустить контейнеры
docker compose restart

# Остановить и удалить (данные сохраняются)
docker compose down

# Удалить всё включая БД
docker compose down -v

# Посмотреть логи
docker compose logs -f web
```

### Django команды

```bash
# Создать миграции
docker compose exec web python manage.py makemigrations

# Применить миграции
docker compose exec web python manage.py migrate

# Django shell
docker compose exec web python manage.py shell

# Собрать статику
docker compose exec web python manage.py collectstatic --noinput

# Проверить проект
docker compose exec web python manage.py check
```

### Работа с PostgreSQL

```bash
# Подключиться к БД
docker compose exec db psql -U notes_user -d notes_db

# Внутри psql:
\dt              # список таблиц
\d notes_note    # структура таблицы
\q               # выход
```

---

## 📊 Модели данных

### User
- `name` — имя пользователя
- `email` — email (уникальный)

### UserProfile (OneToOne с User)
- `bio` — биография
- `birth_date` — дата рождения

### Note
- `text` — текст заметки
- `author` — ForeignKey на User
- `status` — ForeignKey на Status
- `categories` — ManyToMany с Category
- `created_at` — дата создания

### Status
- `name` — название статуса
- `is_final` — финальный статус или нет

### Category
- `title` — название категории

---

## 🎯 Особенности реализации

### Оптимизация запросов
Используются `select_related` и `prefetch_related` для минимизации SQL-запросов:

```python
Note.objects.select_related('author', 'status').prefetch_related('categories')
```

### Пагинация
Список заметок разбит на страницы по 10 элементов с помощью `Paginator`.

### Формы Django
Создание и редактирование заметок через `ModelForm` с валидацией.

### Сообщения
Использование `django.contrib.messages` для уведомлений пользователя.

---

## 🧪 Тестирование

```bash
# Запустить тесты
docker compose exec web python manage.py test

# Проверить количество SQL-запросов
docker compose exec web python manage.py shell
```

```python
from django.db import connection, reset_queries
from notes.models import Note

reset_queries()
notes = list(Note.objects.select_related('author', 'status').prefetch_related('categories')[:10])
for n in notes:
    print(n.author.name, n.status.name, [c.title for c in n.categories.all()])

print(f"SQL запросов: {len(connection.queries)}")  # Должно быть 3-5
```

---

## 📝 Полезные команды

```bash
# Очистить кеш Python
docker compose exec web find . -type d -name __pycache__ -exec rm -r {} +

# Пересоздать БД с нуля
docker compose down -v
docker compose up -d
docker compose exec web python manage.py migrate
docker compose exec web python seed.py

# Экспортировать данные
docker compose exec web python manage.py dumpdata > backup.json

# Импортировать данные
docker compose exec web python manage.py loaddata backup.json
```

---

## 🚧 Возможные улучшения

- [ ] REST API через Django REST Framework
- [ ] Аутентификация и регистрация пользователей
- [ ] Поиск по заметкам
- [ ] Фильтры по статусу и дате
- [ ] Экспорт заметок в PDF/Markdown
- [ ] Прикрепление файлов к заметкам
- [ ] Тесты покрытия (coverage)
- [ ] CI/CD pipeline
- [ ] Деплой на Heroku/DigitalOcean

---

## 👨‍💻 Автор

**Andas Kazybek**


---

## 📄 Лицензия

MIT License