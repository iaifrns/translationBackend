from django.urls import path
from .views import AddContent, DeleteContent, GetContent

urlpatterns = [
    path('addcontent/', AddContent.as_view()),
    path('deletecontent/', DeleteContent.as_view()),
    path('getcontent/', GetContent.as_view())
]