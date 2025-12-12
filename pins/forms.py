from django import forms 
from .models import Pinterest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PinterestForm(forms.ModelForm):
    class Meta:
        model = Pinterest
        fields = ['photo', 'text']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
