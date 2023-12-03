#!/usr/bin/env python3
# @author      Markus Kösters

from django.urls import path, include

urlpatterns = [
    # path("", views.home, name='home'),
    # path('appointment/<int:id>/', views.Appointments.appointment, name='appointment'),
    # path('calendars/', views.Calendars.allCalendars, name='calendarList'),
    # path('calendar/<int:year>/<int:month>/', views.Calendars.calendarPage, name='calendar'),
    # path("CreateCalendar/", views.Calendars.createCalendar, name='createCalendar'),
    # path('CreateAppointment/', views.Appointments.createAppointment, name='createAppointment')
    path('', include(('api.urls', 'api'), namespace='api')),
]
