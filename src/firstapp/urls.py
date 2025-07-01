from django.urls import path

from src.firstapp.views import greetings, hello_view

urlpatterns = [
    path('', greetings),
    # http://127.0.0.1:8000/api/v1/first_app/andrey/
    path('<str:name>/', hello_view),
]
