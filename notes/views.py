from django.shortcuts import get_object_or_404, render
from .models import Note, User

def index(request):
    notes = (
        Note.objects
        .select_related('author', 'status')
        .prefetch_related('categories')
        .order_by('-created_at')
    )
    return render(request, 'notes/index.html', {'notes': notes})

def note_detail(request, note_id: int):
    qs = (
        Note.objects
        .select_related('author', 'status', 'author__userprofile')
        .prefetch_related('categories')
    )
    note = get_object_or_404(qs, pk=note_id)
    profile = getattr(note.author, "userprofile", None)
    return render(request, 'notes/note_detail.html', {'note': note, 'profile': profile})

def user_detail(request, user_id: int):
    user = get_object_or_404(User.objects.select_related('userprofile'), pk=user_id)
    profile = getattr(user, "userprofile", None)
    user_notes = (
        Note.objects
        .filter(author=user)
        .select_related('status')
        .order_by('-created_at')
    )
    return render(request, 'notes/user_detail.html', {'user': user, 'profile': profile, 'notes': user_notes})

def users_list(request):
    users = User.objects.all().order_by('name')
    return render(request, 'notes/users_list.html', {'users': users})
