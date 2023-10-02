from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
from django.forms import widgets


class CustomerRegistrationForm(forms.ModelForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email= forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model=Customer
        fields=["username", "password", "email", "full_name","address","mobile"]
        widgets= {
            'full_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Full Name..'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter address..'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter mobile number..'}),
        }

    def clean_username(self):
        uname=self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Customer with this username  already exists.")
        return uname

    def clean_email(self):
        em=self.cleaned_data.get("email")
        if User.objects.filter(email=em).exists():
            raise forms.ValidationError("Customer with this email already exists.")
        return em
    


class CustomerLoginForm(forms.Form):
    username= forms.CharField(widget=widgets.TextInput(attrs={'class':'form-control','placeholder':'Enter the username...'}))
    password= forms.CharField(widget=widgets.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the password...'}))

class PasswordForgotForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Enter the email used in customer account..."
    }))

    def clean_email(self):
        e = self.cleaned_data.get("email")
        if Customer.objects.filter(user__email=e).exists():
            pass
        else:
            raise forms.ValidationError(
                "Customer with this account does not exists..")
        return e
    

class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'autocomplete': 'new-password',
        'placeholder': 'Enter New Password',
    }), label="New Password")
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'autocomplete': 'new-password',
        'placeholder': 'Confirm New Password',
    }), label="Confirm New Password")

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        confirm_new_password = self.cleaned_data.get("confirm_new_password")
        if new_password != confirm_new_password:
            raise forms.ValidationError(
                "New Passwords did not match!")
        return confirm_new_password


