from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime

from accounts.models import UserProfile
from .tokens import account_activation_token


# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        full_name = request.POST['full_name']
        gender = request.POST['gender']
        mobile = request.POST.get('mobile')
        dob_input = request.POST.get('dob')
        dob = datetime.strptime(dob_input, "%Y-%m-%d").date() if dob_input else None

      
        user = User.objects.create_user(username=username, password=password, email=email, is_active=False)

        if not user.is_staff:

          profile, created = UserProfile.objects.get_or_create(user=user)
          profile.full_name = full_name
          profile.gender = gender
          profile.mobile = mobile
          profile.dob = dob
          profile.save()
 

        send_activation_email(user, request)

        messages.success(request, "Account created! Please check your email to activate.")
        return redirect('login')

    return render(request, 'accounts/signup.html')

#login view

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if not user.is_active:
                messages.error(request, "Please activate your account via email.")
                return redirect('login')
            login(request, user)
            return redirect('library_home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('welcome_page')


def send_activation_email(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    activation_link = request.build_absolute_uri(
        reverse('activate', kwargs={'uidb64': uid, 'token': token})
    )

    subject = "Activate your E-Library Account"
    message = render_to_string('accounts/activation_email.html', {
        'user': user,
        'activation_link': activation_link,
    })

    send_mail(subject, message, None, [user.email])



def activate_account(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account activated! You can now login.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')
        return redirect('login')

