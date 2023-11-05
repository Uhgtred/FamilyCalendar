#!/usr/bin/env python3
# @author      Markus Kösters

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('calendars/', views.Calendars.allCalendars, name='calendarList'),
    path('calendar/<int:year>/', views.Calendars.calendarPage, name='calendar'),
    path("CreateCalendar/", views.createCalendar, name='createCalendar'),
    path('CreateAppointment/', views.createAppointment, name='createAppointment')
]
