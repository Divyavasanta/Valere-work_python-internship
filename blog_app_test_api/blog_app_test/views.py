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
from rest_framework import viewsets
from .models import Article
from .serializer import ArticleSerializer
from rest_framework.views import APIView
from .serializer import RegisterSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .forms import UserRegistrationForm

User = get_user_model()
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializer import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"})
        return Response({"error": "Invalid credentials"}, status=400)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out"})


class ProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


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
                'noreply@mysite.com',  # Replace with your sender email if needed
                [user.email]
            )
            email.content_subtype = "html"

            try:
                email.send()
                messages.success(request, 'Please check your email to activate your account.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Email sending failed: {e}')
                return render(request, 'blog/signup.html', {'form': form})
        else:
            print(form.errors)  # Debugging
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

#api view:
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
