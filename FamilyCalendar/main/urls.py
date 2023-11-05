#!/usr/bin/env python3
# @author      Markus Kösters

from django.urls import path
from . import views

urlpatterns = [
    path('appointment/', views.calendarPage, name='calendarPage'),
    path("", views.home, name='home'),
    path('calendar/<int:year>/', views.calendarPage, name='calendar'),
    path("CreateCalendar/", views.createCalendar, name='createCalendar'),
    path('CreateAppointment/', views.createAppointment, name='createAppointment')
]
