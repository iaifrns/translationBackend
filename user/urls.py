from django.urls import path
from .views import Login, Register, getUser

urlpatterns = [
    path('login/', Login.as_view()),
    path('register/', Register.as_view()),
    path('getUser/', getUser.as_view()),
]