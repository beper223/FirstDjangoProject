from django.shortcuts import render
from django.http import HttpResponse

def greetings(request):
    return HttpResponse("<h1>Hello, world!</h1>")

def hello_view(request, name):
    return HttpResponse(f"<h1>Hello, {name}</h1>")
