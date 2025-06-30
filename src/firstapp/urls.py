from django.urls import path

from src.firstapp.views import greetings, hello_view

urlpatterns = [
    path('', greetings),
    path('<str:name>/', hello_view),
]
