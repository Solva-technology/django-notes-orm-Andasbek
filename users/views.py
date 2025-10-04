from django.shortcuts import render, get_object_or_404
from notes.models import User, Note


def user_list(request):
    users = User.objects.all().order_by('name')
    return render(request, 'users/list.html', {'users': users})


def user_detail(request, pk):
    user = get_object_or_404(
        User.objects.select_related('profile'),  # изменено
        pk=pk
    )
    
    profile = getattr(user, 'profile', None)  # изменено
    
    notes = (
        Note.objects
        .filter(author=user)
        .select_related('status')
        .prefetch_related('categories')
        .order_by('-created_at')
    )
    
    return render(request, 'users/detail.html', {
        'user': user,
        'profile': profile,
        'notes': notes
    })