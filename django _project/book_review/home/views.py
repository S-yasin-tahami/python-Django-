from django.shortcuts import render
from add.models import Book

def home(request):
    return render(request, 'home.html')

def browse_books(request):
    book_info = Book.objects.all()
    return render(request, 'browse_books.html', {'book_info':book_info})
