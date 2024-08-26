# users/forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import *
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@duocuc.cl') and not email.endswith('@profesor.duoc.cl'):
            raise ValidationError('El correo debe ser @duoc o @profesor.duoc')
        return email


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']