from django.urls import path
from .views import addFeature, deleteFeature, getAllFeatures, getOneFeature

urlpatterns = [
    path('add/', addFeature.as_view()),
    path('getOne/', getOneFeature.as_view()),
    path('getAll/', getAllFeatures.as_view()),
    path('delete/', deleteFeature.as_view())
]