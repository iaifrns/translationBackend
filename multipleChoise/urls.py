from django.urls import path
from .views import addChoise, getOneChoise, getAllChoise, deleteChoise

urlpatterns = [
    path('add/', addChoise.as_view()),
    path('getOne/', getOneChoise.as_view()),
    path('getAll/', getAllChoise.as_view()),
    path('delete/', deleteChoise.as_view())
]