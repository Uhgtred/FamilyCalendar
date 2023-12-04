#!/usr/bin/env python3
# @author: Markus Kösters
import sys

from django.urls import path
from api import views

urlpatterns = [
    path("", views.home, name='home'),
    path('appointment/<int:id>/', views.Appointments.appointment, name='appointment'),
    path('calendars/', views.Calendars.allCalendars, name='calendarList'),
    path('calendar/<int:year>/<int:month>/', views.Calendars.calendarPage, name='calendar'),
    path("CreateCalendar/", views.Calendars.createCalendar, name='createCalendar'),
    path('CreateAppointment/', views.Appointments.createAppointment, name='createAppointment')
]
