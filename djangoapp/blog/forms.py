from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User  

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
        label='Password'
    )

    date_of_birth = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'})
    )

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'mobile_number', 'date_of_birth', 'gender', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Secure password hash
        if commit:
            user.save()
        return user
