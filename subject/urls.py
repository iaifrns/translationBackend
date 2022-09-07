from django.urls import path
from .views import addSubject, getSubjects, deleteSubject

urlpatterns = [
    path('add/', addSubject.as_view()),
    path('getall/', getSubjects.as_view()),
    path('delete/', deleteSubject.as_view())
]