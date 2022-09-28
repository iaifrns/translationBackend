from django.urls import path
from .views import Login, Register, getUser, getUsers

urlpatterns = [
    path('login/', Login.as_view()),
    path('register/', Register.as_view()),
    path('getUser/', getUser.as_view()),
    path('getUsers/', getUsers.as_view()),
]