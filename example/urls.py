# example/urls.py
from django.urls import path
from example.views import *


urlpatterns = [
    path('', index),
    path('ip/', ip),
]
