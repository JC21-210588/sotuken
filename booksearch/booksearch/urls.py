# booksearch/urls.py
from django.contrib import admin
from django.urls import path
from books.views import search_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_books, name='search_books'),
    path('', search_books, name='default_search'),  # デフォルトのパスに対する処理を追加
]
