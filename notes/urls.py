from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/', views.users_list, name='users_list'),
]