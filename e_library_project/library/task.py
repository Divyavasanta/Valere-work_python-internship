from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task
def send_admin_notification(username, book_title, action_type):
    subject = f"{username} {action_type}ed a book"
    message = f"{username} has {action_type}ed the book titled '{book_title}'."

    admin_emails = User.objects.filter(is_superuser=True).values_list('email', flat=True)

    send_mail(
        subject,
        message,
        'dvasanta05@gmail.com', 
        admin_emails,
        fail_silently=False,
    )
