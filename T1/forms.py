from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#class UserForm(forms.ModelForm):
    # class Meta:
    #     model_name='register'
    #     widgets = {
    #         'password': forms.PasswordInput(),
    #     }
    #     fields = ("internationalID","username","birthdate")


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=24)
    password = forms.CharField(widget=forms.PasswordInput())