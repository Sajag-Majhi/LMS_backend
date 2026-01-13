from django.urls import path
from .views import Read,Home,Write,Delete

urlpatterns = [
    path('',Home, name='home'),
    path('read/',Read, name='read'),
    path('write/',Write, name='write'),
    path('delete/', Delete, name='delete'),
]
