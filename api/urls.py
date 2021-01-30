from django.urls import path
from .views import Hi
urlpatterns = [
    path("", Hi)
]

