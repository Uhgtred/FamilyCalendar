#!/usr/bin/env python3
# @author      Markus Kösters

from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.calendarPage, name='calendarPage'),
    path("", views.home, name='home'),
    path("CreateCalendar/", views.createCalendar, name='createCalendar')
]
