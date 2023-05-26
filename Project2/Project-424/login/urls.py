from django.urls import path
from . import views

urlpatterns = [
    path('logina' , views.logina , name='index')
]