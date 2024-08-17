from .models import Todo
from django import forms
from django.contrib.auth.models import User

class Todo_creation_form(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title', 'discription', 'image']

class Login_form(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields=['username', 'password']