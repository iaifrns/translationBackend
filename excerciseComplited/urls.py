from django.urls import path
from .views import addComplitedExercise, getOneComplitedExercise, getAllCompliteExercise

urlpatterns = [
    path('add/', addComplitedExercise.as_view()),
    path('getOne/', getOneComplitedExercise.as_view()),
    path('getAll/', getAllCompliteExercise.as_view())
]