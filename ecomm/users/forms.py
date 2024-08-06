from django import forms 

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 


class NewRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True )
    username = forms.CharField(required=True)  
    password1 = forms.CharField(required=True, widget= forms.PasswordInput()) 
    password2 = forms.CharField(required=True, widget=forms.PasswordInput()) 

    class Meta:
        model = User 
        fields = ['email', 'username', 'password1', 'password2']

