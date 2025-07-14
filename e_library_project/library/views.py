from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Book, Bookmark, Notification
from django.shortcuts import render, get_object_or_404 
from django.http import JsonResponse, FileResponse, Http404   
import os
import mimetypes
from django.db.models import Q
from django.core.paginator import Paginator
from .models import ActivityLog
from .task import send_admin_notification


def library_home(request):
    query = request.GET.get('q', '')
    selected_author = request.GET.get('author', '')
    show_bookmarked = request.GET.get('bookmarked', '') == '1'

    books = Book.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))

    if selected_author:
        books = books.filter(author=selected_author)

    if show_bookmarked and request.user.is_authenticated:
        bookmarked_ids = Bookmark.objects.filter(user=request.user).values_list('book_id', flat=True)
        books = books.filter(id__in=bookmarked_ids)
    else:
        bookmarked_ids = []
        if request.user.is_authenticated:
            bookmarked_ids = Bookmark.objects.filter(user=request.user).values_list('book_id', flat=True)

   
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    authors = Book.objects.values_list('author', flat=True).distinct()

    
    unseen_count = 0
    if request.user.is_authenticated:
        unseen_count = Notification.objects.filter(user=request.user, seen=False).count()


    return render(request, 'library/book_list.html', {
        'page_obj': page_obj,
        'bookmarked_ids': bookmarked_ids,
        'query': query,
        'authors': authors,
        'selected_author': selected_author,
        'show_bookmarked': show_bookmarked,
        'unseen_count': unseen_count,
    })

def welcome_page(request):
    books = Book.objects.all()[:5]  
    return render(request, 'library/welcome.html', {'books': books})

@login_required
def toggle_bookmark(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, id=book_id)
        bookmark, created = Bookmark.objects.get_or_create(user=request.user, book=book)
        if not created:
            bookmark.delete()
            ActivityLog.objects.create(
                user=request.user,
                event_type='unbookmark', 
                book=book,
            )
        else:
         
            ActivityLog.objects.create(
                user=request.user,
                event_type='bookmark',
                book=book,
            )

           
            send_admin_notification.delay(
                request.user.username,
                book.title,
                'bookmark'
            )

        return redirect('library_home')


@login_required
def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.download_count += 1
    book.save()

    ActivityLog.objects.create(
        user=request.user,
        book=book,
        event_type='download'
    )

   
    send_admin_notification.delay(
        request.user.username,
        book.title,
        'download'
    )

    response = FileResponse(book.pdf_file.open('rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{book.title}.pdf"'
    return response




@login_required
def my_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user).select_related('book')
    return render(request, 'library/my_bookmarks.html', {'bookmarks': bookmarks})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    absolute_pdf_url = request.build_absolute_uri(book.pdf_file.url)
    
    bookmarked = False
    if request.user.is_authenticated:
        bookmarked = Bookmark.objects.filter(user=request.user, book=book).exists()

    return render(request, 'library/book_detail.html', {
        'book': book,
        'bookmarked': bookmarked,
        'absolute_pdf_url': absolute_pdf_url,  
    })

# library/views.py


@login_required
def fetch_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')[:10]

    
    Notification.objects.filter(user=request.user, seen=False).update(seen=True)

    data = {
        'notifications': [
            {
                'message': n.message,
                'book_id': n.book.id if n.book else None
            }
            for n in notifications
        ]
    }
    return JsonResponse(data)


@login_required
def mark_notifications_seen(request):
    ActivityLog.objects.filter(user=request.user, seen=False).update(seen=True)
    return JsonResponse({'status': 'success'})