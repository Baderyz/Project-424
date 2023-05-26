from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django import forms


# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=18, validators=[MinLengthValidator(1)])
    password = models.CharField(max_length=24, validators=[MinLengthValidator(8)])
    birthdate = models.DateField()
    internationalID = models.IntegerField(
        validators=[MinLengthValidator(10), MaxLengthValidator(10)])

    def __str__(self):
        return f'ID: {self.internationalID} Name: {self.username} Birth Date : {self.birthdate}'
