from django.urls import path
from . import views
from .views import welcome_page
from .views import toggle_bookmark

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('library/', views.library_home, name='library_home'),
    path('toggle-bookmark/', views.toggle_bookmark, name='toggle_bookmark'),

    path('my-bookmarks/', views.my_bookmarks, name='my_bookmarks'),
    path('download/<int:book_id>/', views.download_book, name='download_book'),  
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    

]
