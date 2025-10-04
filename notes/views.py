from django.contrib import messages
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note, User, Category


def index(request):
    qs = (
        Note.objects
        .select_related("author", "status")
        .prefetch_related("categories")
        .order_by("-created_at")
    )
    paginator = Paginator(qs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "notes/index.html", {"page_obj": page_obj})


def note_detail(request, note_id: int):
    qs = (
        Note.objects
        .select_related("author", "status", "author__profile")
        .prefetch_related("categories")
    )
    note = get_object_or_404(qs, pk=note_id)
    profile = getattr(note.author, "profile", None)
    return render(request, "notes/note_detail.html", {"note": note, "profile": profile})


@transaction.atomic
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            messages.success(request, f"Заметка #{note.id} создана.")
            return redirect("notes:note_detail", note_id=note.id)
        messages.error(request, "Пожалуйста, исправьте ошибки формы.")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form, "mode": "create"})


@transaction.atomic
def note_edit(request, note_id: int):
    note = get_object_or_404(
        Note.objects.select_related("author", "status").prefetch_related("categories"),
        pk=note_id
    )
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            messages.success(request, f"Заметка #{note.id} обновлена.")
            return redirect("notes:note_detail", note_id=note.id)
        messages.error(request, "Пожалуйста, исправьте ошибки формы.")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form, "mode": "edit", "note": note})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'notes/categories.html', {'categories': categories})


def category_notes(request, category_id: int):
    category = get_object_or_404(Category, pk=category_id)
    notes = (
        Note.objects
        .filter(categories=category)
        .select_related('author', 'status')
        .prefetch_related('categories')
        .order_by('-created_at')
    )
    return render(request, 'notes/category_notes.html', {
        'category': category,
        'notes': notes
    })