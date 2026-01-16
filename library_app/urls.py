from django.urls import path
from .views import Read,Home,Write,Delete,Update,EditUser,EditBook

urlpatterns = [
    path('',Home, name='home'),
    path('read/',Read, name='read'),
    path('write/',Write, name='write'),
    path('delete/', Delete, name='delete'),
    path('update/', Update, name='update'),
    path('edit/user/<int:user_id>/',EditUser, name='edit_user'),
    path('edit/book/<int:book_id>/',EditBook, name='edit_book'),
]
