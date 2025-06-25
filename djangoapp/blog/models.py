import uuid
from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.
#user model

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, name, mobile_number, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            name=name,
            mobile_number=mobile_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, name, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, name, mobile_number, password, **extra_fields)

    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.CharField(max_length=150, unique=True)  
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile_number = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('Male','Male'), ('Female','Female')), null=True, blank=True)

    last_login = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'   
    REQUIRED_FIELDS = ['email', 'name', 'mobile_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.username 


# Post Category model
class PostCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name


# Tag model (used for Many-to-Many with Post)
class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Post model
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Many-to-One relationship with User
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # Many-to-One
    
    title = models.CharField(max_length=255)
    body = models.TextField()
    publish_date = models.DateField()
    created_at = models.TimeField()
    
    # Many-to-One relationship with PostCategory
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True, related_name='posts')  # Many-to-One
    
    # Many-to-Many relationship with Tag
    tags = models.ManyToManyField(Tag, blank=True)  # Many-to-Many

    # Instagram-like caption field with max 2200 characters
    caption = models.TextField(validators=[MaxLengthValidator(2200)])  # Instagram-style

    def __str__(self):
        return self.title


# PostStatistics model (One-to-One with Post)
class PostStatistics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # One-to-One relationship with Post
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='statistics')  # One-to-One
    
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)


# Comment model
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Many-to-One relationship with User
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # Many-to-One
    
    # Many-to-One relationship with Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Many-to-One
    
    comment_text = models.TextField()
    timestamp = models.DateTimeField()
    
    # Recursive relationship (self-referencing)
    parent_comment = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )  # Recursive relationship (self)


# CommentLike model
class CommentLike(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Many-to-One with Comment
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')  # Many-to-One
    
    # Many-to-One with User
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Many-to-One
    
    timestamp = models.DateTimeField()


# PostLike model
class PostLike(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Many-to-One with User
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Many-to-One
    
    # Many-to-One with Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')  # Many-to-One
    
    timestamp = models.DateTimeField()


# Notification model
class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Many-to-One with User
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')  # Many-to-One
    
    # Generic UUID reference to trigger (could be a Post, Comment, etc.)
    triggered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='triggered_notifications', null=True, blank=True)


    
    timestamp = models.DateTimeField()
