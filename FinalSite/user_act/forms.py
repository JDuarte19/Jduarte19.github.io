from django import forms
from django.contrib.auth.models import User
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["user_name","email","password"]
        labels = {
            'user_name': 'Username',
            'email': 'Email',
            'password': 'Password'
        }

        widgets = {
            'user_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.TextInput(attrs={'class':'form-control'}),
        }