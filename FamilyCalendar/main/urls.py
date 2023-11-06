#!/usr/bin/env python3
# @author      Markus Kösters

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('appointment/<str:name>/', views.Appointments.appointment, name='appointment'),
    path('calendars/', views.Calendars.allCalendars, name='calendarList'),
    path('calendar/<int:year>/', views.Calendars.calendarPage, name='calendar'),
    path("CreateCalendar/", views.Calendars.createCalendar, name='createCalendar'),
    path('CreateAppointment/', views.Appointments.createAppointment, name='createAppointment')
]
