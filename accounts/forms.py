from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    
    first_name=forms.CharField(max_length=30, required=False,help_text="Optional")
    last_name=forms.CharField(max_length=30, required=False,help_text="Optional")
    email=forms.EmailField(max_length=254,required=True,)
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}))
    class Meta: 
        model=User
        fields = ['username','first_name','last_name','email','password1','password2']


# class LoginForm(forms.Form):
#     username= forms.CharField()
#     password =forms.CharField(widget=forms.PasswordInput)