from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('feed/', views.feed_view, name='feed'),
    path('add-media/', views.add_media_view, name='add_media'),
    path('profile/<uuid:user_id>/', views.profile_view, name='profile'),
    path('messages/', views.messages_view, name='messages'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
