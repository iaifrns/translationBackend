from django.urls import path
from .views import addLevel, getOneLevel, getAllLevel, deleteLevel

urlpatterns = [
    path('add/', addLevel.as_view()),
    path('getOne/', getOneLevel.as_view()),
    path('getAll/', getAllLevel.as_view()),
    path('delete/', deleteLevel.as_view())
]
