from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class UserForm(forms.ModelForm):
# class Meta:
#     model_name='register'
#     widgets = {
#         'password': forms.PasswordInput(),
#     }
#     fields = ("internationalID","username","birthdate")


class RegisterForm(UserCreationForm):
    model = User
    username = forms.CharField(max_length=24)
    password = forms.CharField(widget=forms.PasswordInput())


from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
