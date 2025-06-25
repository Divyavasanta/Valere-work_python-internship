from django.contrib import admin
from .models import (User, PostCategory, Tag, Post, PostStatistics, Comment, CommentLike, PostLike, Notification)

# Register your models here.
admin.site.register(User)
admin.site.register(PostCategory)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(PostStatistics)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(PostLike)
admin.site.register(Notification)