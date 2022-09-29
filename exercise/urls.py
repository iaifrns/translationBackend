from django.urls import path
from .views import addExercise, getOneExercise, getAllExercise, deleteExercise

urlpatterns = [
    path('add/', addExercise.as_view()),
    path('getOne/', getOneExercise.as_view()),
    path('getAll/', getAllExercise.as_view()),
    path('delete/', deleteExercise.as_view())
]
