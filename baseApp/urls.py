from django.contrib import admin
from django.urls import path
from baseApp.views import *

urlpatterns = [
    path('', home, name='home'),
]
