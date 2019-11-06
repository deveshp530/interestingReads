from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

def book_detail(request, pk):
    books = Book.objects.get(id=pk)
    return render(request, 'book_detail.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def edit_book(request,pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def delete_book(request,pk):
    Book.objects.get(id=pk).delete()
    return redirect('list_books')
