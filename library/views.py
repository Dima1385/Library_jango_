
from django.shortcuts import render

def home(request):

    return render(request, 'home.html')

def books(request):
    return render(request, 'books.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')