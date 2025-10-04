# seed.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notebook_project.settings')
django.setup()

from notes.models import User, UserProfile, Status, Category, Note
from datetime import date

# Создаем статусы
statuses = [
    Status.objects.get_or_create(name="Черновик", is_final=False)[0],
    Status.objects.get_or_create(name="Опубликовано", is_final=True)[0],
    Status.objects.get_or_create(name="Архив", is_final=True)[0],
]

# Создаем категории
categories = [
    Category.objects.get_or_create(title="Работа")[0],
    Category.objects.get_or_create(title="Личное")[0],
    Category.objects.get_or_create(title="Идеи")[0],
]

# Создаем пользователей
users = []
for i in range(1, 4):
    user, created = User.objects.get_or_create(
        email=f"user{i}@example.com",
        defaults={"name": f"Пользователь {i}"}
    )
    UserProfile.objects.get_or_create(
        user=user,
        defaults={
            "bio": f"Биография пользователя {i}",
            "birth_date": date(1990, 1, i)
        }
    )
    users.append(user)

# Создаем заметки
for i in range(1, 11):
    note, created = Note.objects.get_or_create(
        text=f"Текст заметки номер {i}",
        author=users[i % 3],
        status=statuses[i % 3]
    )
    note.categories.set([categories[i % 3]])

print("✅ База данных заполнена тестовыми данными!")