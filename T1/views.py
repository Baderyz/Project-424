from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
import django.contrib
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data(['username'])
            password = form.cleaned_data(['password1'])
            messages.success(request, 'Registration successful')
            return reverse()
    else:
        form = UserCreationForm(request.POST)

    return render(request, 'T1/register.html', {"form": form})


class Register(forms.Form):
    username = forms.CharField(label='User Name:')
    password = forms.CharField(widget=forms.PasswordInput(),label='Password:')
    birthdate = forms.DateField(label='Birth Date:')
    unique_id = forms.CharField(max_length=10, label='ID:')
