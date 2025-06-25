from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator

from .forms import UserRegistrationForm

User = get_user_model()

# Create your views here.
from django.http import HttpResponse


def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'blog/dashboard.html')  
    else:
        return render(request, 'blog/welcome.html') 
    
def feed_view(request):
    return render(request, 'blog/feed.html')  

def add_media_view(request):
    return render(request, 'blog/add_media.html')

def profile_view(request, user_id):
    return render(request, 'blog/profile.html', {'user_id': user_id})

def messages_view(request):
    return render(request, 'blog/messages.html')

def notifications_view(request):
    return render(request, 'blog/notifications.html')

    

# Sign Up
def user_signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()


            # verification email
        
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = request.build_absolute_uri(f'/activate/{uid}/{token}/')

            subject = 'Verify your email address'
            context = {
                 'username': user.username,
                 'activation_link': activation_link
                }

            html_message = render_to_string('blog/activation_email.html', context)

            email = EmailMessage(
                subject,
                html_message,
                'noreply@mysite.com',
                [user.email]
            )
            email.content_subtype = "html"
            email.send()

            messages.success(request, 'Please check your email to activate your account.')
            return redirect('login')
    else:   
         form = UserRegistrationForm()

    return render(request, 'blog/signup.html', {'form': form})

# Activate email
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account activated successfully. You can now log in.')
        return redirect('login')
    else:
        return render(request, 'blog/activation_failed.html')

# Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password=password)  # if using custom user with email login
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials or inactive account')
    return render(request, 'blog/login.html')

# Logout
def user_logout(request):
    logout(request)
    return redirect('login')
