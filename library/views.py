
from django.shortcuts import render
from .models import Book
from .models import Author



books_db = [
    {"id": 1, "title": "Harry Potter", "author": "J.K. Rowling", "description": "A book about a young wizard."},
    {"id": 2, "title": "Game of Thrones", "author": "George R.R. Martin", "description": "A series about the battle for the Iron Throne."},
    {"id": 3, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "description": "A series about the journey to destroy a powerful ring."}
]

authors_db = [
    {"id": 1, "name": "J.K. Rowling", "bio": "J.K. Rowling is a British author, best known for writing the Harry Potter series.", "books": ["Harry Potter"]},
    {"id": 2, "name": "George R.R. Martin", "bio": "George R.R. Martin is an American novelist, famous for his epic fantasy series A Song of Ice and Fire.", "books": ["Game of Thrones"]},
    {"id": 3, "name": "J.R.R. Tolkien", "bio": "J.R.R. Tolkien was an English writer and professor, best known for The Hobbit and The Lord of the Rings.", "books": ["The Lord of the Rings"]},
]

def home(request):
    return render(request, 'home.html')

def books(request):
    return render(request, 'books_list.html', {'books': books_db})

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def authors(request):
    return render(request, 'authors_list.html', {'authors': authors_db})

def book_detail(request, book_id):
    book = next((book for book in books_db if book["id"] == book_id), None)
    return render(request, 'book_detail.html', {'book': book})

def author_detail(request, author_id):
    author = next((a for a in authors_db if a['id'] == author_id), None)
    if author:
        return render(request, 'author_detail.html', {'author': author})
    return render(request, '404.html')