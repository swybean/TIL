from django.shortcuts import render
from .models import Book, Review

# Create your views here.

def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }

    return render(request, 'libraries/index.html', context)


def detail(requset, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
    }

    return render(requset, 'libraries/detail.html', context)

