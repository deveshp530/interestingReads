from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('books/<int:pk>', views.book_detail, name='book_detail'),
    path('book/new', views.create_book, name='create_book'),
    path('book/<int:pk>/edit', views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete', views.delete_book, name='delete_book'),



]