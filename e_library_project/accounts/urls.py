from django.urls import path
from . import views
from .views import activate_account


urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
]
