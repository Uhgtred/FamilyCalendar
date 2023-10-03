#!/usr/bin/env python3
# @author      Markus Kösters

from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='index')
]