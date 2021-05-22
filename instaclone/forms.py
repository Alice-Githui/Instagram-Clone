from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Image, Comment

class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]

class NewImageForm(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['comments','likes','profile']
        
