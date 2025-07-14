from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bookmark, ActivityLog
from django.contrib.auth.models import User
from .models import Book
from .models import Notification 

@receiver(post_save, sender = Bookmark)
def log_bookmark_event(sender, instance, created, **kwargs):
    if created:
        ActivityLog.objects.create(
                user = instance.user,
                book = instance.book,
                event_type = 'bookmark'
            
            )

        
@receiver(post_save, sender=Book)
def notify_users_on_new_book(sender, instance, created, **kwargs):
    if created:
        users = User.objects.filter(is_staff=False, is_active=True)
        for user in users:
            Notification.objects.create(
                user=user,
                message=f"New book uploaded: {instance.title}",
            )