from django.urls import path
from .views import addCategory, getOneCategory, getAllCategories, deleteCategory

urlpatterns = [
    path('add/', addCategory.as_view()),
    path('deleteCategory/', deleteCategory.as_view()),
    path('getOne/', getOneCategory.as_view()),
    path('getAll/', getAllCategories.as_view()),
]