from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

books_db = [
    {
        "id": 1,
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "description": "A book about a young wizard.",
        "image": "images/harry_potter.jpg"
    },
    {
        "id": 2,
        "title": "Game of Thrones",
        "author": "George R.R. Martin",
        "description": "A series about the battle for the Iron Throne.",
        "image": "images/game_of_thrones.jpg"
    },
    {
        "id": 3,
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "description": "A series about the journey to destroy a powerful ring.",
        "image": "images/lord_of_the_rings.jpg"
    }
]


authors_db = [
    {"id": 1, "name": "J.K. Rowling", "bio": "J.K. Rowling is a British author, best known for writing the Harry Potter series.", "books": ["Harry Potter"]},
    {"id": 2, "name": "George R.R. Martin", "bio": "George R.R. Martin is an American novelist, famous for his epic fantasy series A Song of Ice and Fire.", "books": ["Game of Thrones"]},
    {"id": 3, "name": "J.R.R. Tolkien", "bio": "J.R.R. Tolkien was an English writer and professor, best known for The Hobbit and The Lord of the Rings.", "books": ["The Lord of the Rings"]},
]


# Реєстрація
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Реєстрація успішна! Ви можете увійти.')
            return redirect('login')
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# Вхід
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

# Вихід
def logout_view(request):
    logout(request)
    return redirect('home')


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
    if book:
        author = next((a for a in authors_db if a["name"] == book["author"]), None)
        book["author_id"] = author["id"] if author else None
    return render(request, 'book_detail.html', {'book': book})


def author_detail(request, author_id):
    author = next((a for a in authors_db if a['id'] == author_id), None)
    if author:
        return render(request, 'author_detail.html', {'author': author})
    return render(request, '404.html')



# @login_required
# def books(request):
#     return render(request, 'books.html')

# @login_required
# def authors(request):
#     return render(request, 'authors.html')

