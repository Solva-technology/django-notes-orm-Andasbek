from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.note_create, name="note_create"),
    path("categories/", views.category_list, name="category_list"),  # добавить
    path("categories/<int:category_id>/", views.category_notes, name="category_notes"),  # добавить
    path("<int:note_id>/", views.note_detail, name="note_detail"),
    path("<int:note_id>/edit/", views.note_edit, name="note_edit"),
]