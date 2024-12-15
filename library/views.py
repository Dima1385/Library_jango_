
from django.shortcuts import render

def home(request):

    return render(request, 'home.html')

def books(request):
    return render(request, 'books.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def authors(request):
    authors_list = [
        {"name": "J.K. Rowling", "books": ["Harry Potter Series"]},
        {"name": "George R.R. Martin", "books": ["A Song of Ice and Fire"]},
        {"name": "J.R.R. Tolkien", "books": ["The Lord of the Rings"]},
    ]
    return render(request, 'authors.html', {'authors': authors_list})
