from django.urls import path
from .views import AddTitle, GetTitles, DeleteTitle

urlpatterns = [
    path('add/', AddTitle.as_view()),
    path('get/', GetTitles.as_view()),
    path('delete/', DeleteTitle.as_view()),
]