#!/usr/bin/env python3
# @author      Markus Kösters

from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>', views.mainPage, name='mainPage')
]