from django.shortcuts import render, get_object_or_404
from notes.models import User

def user_list(request):
    users = User.objects.all().order_by('username')
    return render(request, 'users/list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    notes = user.notes.all()
    return render(request, 'users/detail.html', {
        'user': user,
        'notes': notes
    })