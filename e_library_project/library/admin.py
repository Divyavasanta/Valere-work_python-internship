from django.contrib import admin
from .models import Book
from .models import Bookmark


# Register your models here.

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'uploaded_by', 'download_count', 'created_at')
    search_fields = ('title', 'author')


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'created_at')
    search_fields = ('user__username', 'book__title')

