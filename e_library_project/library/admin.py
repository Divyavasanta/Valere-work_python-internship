from django.contrib import admin
from .models import Book
from .models import Bookmark
from .models import ActivityLog

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'uploaded_by', 'download_count', 'created_at')
    search_fields = ('title', 'author')


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'created_at')
    search_fields = ('user__username', 'book__title')

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_type', 'book', 'timestamp','message', 'seen')
    list_filter = ('event_type', 'timestamp','seen')
    search_fields = ('user_username', 'book_title')