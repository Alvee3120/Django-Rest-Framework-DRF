from django.urls import path
from .views import get_user,create_user

urlpatterns = [
    path('users/', get_user, name = 'get_user'),
    path('users/create', create_user, name = 'create_user'),


]