from django.db import models

# Create your models here.
from django.contrib.auth.models import User

def pdf_upload_path(instance, filename):
    return f'books/pdfs/{filename}'

def thumbnail_upload_path(instance, filename):
    return f'books/thumbnails/{filename}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to=pdf_upload_path)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    download_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')  

    def __str__(self):
        return f"{self.user.username} bookmarked {self.book.title}"


class ActivityLog(models.Model):
    EVENT_CHOICES = [
        ('download', 'Download'),
        ('bookmark', 'Bookmark'),
        ('unbookmark', 'Unbookmark'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    message = models.TextField(default='No message')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.event_type} for {self.user.username}: {self.message}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True) 
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False) 
    
    def __str__(self):
        return f"{self.user.username}: {self.message}"
