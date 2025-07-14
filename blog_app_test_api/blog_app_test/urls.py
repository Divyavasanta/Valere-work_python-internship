from django.urls import path
from . import views
from .views import CustomAuthToken
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog_app_test.views import ArticleViewSet
from .views import RegisterView, LoginView, LogoutView, ProfileView

router = DefaultRouter()
router.register(r'article', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
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
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('token-login/', CustomAuthToken.as_view(), name='token_login'),
    
]
