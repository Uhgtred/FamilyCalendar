import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Calendar, Appointment
from .forms import CreateCalendar, CreateAppointment


# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})

class Calendars:

    @staticmethod
    def calendarPage(response, year: int):
        calendar = Calendar.objects.get(year=year)
        return render(response, 'main/calendar.html', {'list': calendar, 'filter': True})

    @staticmethod
    def allCalendars(response):
        calendars = Calendar.objects.all()
        return render(response, 'main/allCalendars.html', {'list': calendars})


def createAppointment(response):
    if response.method == 'POST':
        form = CreateAppointment(response.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            persons = form.cleaned_data['persons']
            calendar = Calendar.objects.get(year=date.year)
            calendar.appointment_set.create(name=name, description=description, date=[date.day, date.month],
                                               persons=persons)
        return render(response, 'main/calendar.html', {'list': calendar})
    else:
        form = CreateAppointment()
    return render(response, 'main/createAppointment.html', {'form': form})


def createCalendar(response):
    if response.method == 'POST':
        form = CreateCalendar(response.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            calendar = Calendar(year=year)
            calendar.save()
        return HttpResponseRedirect("%i" % calendar.id)
    else:
        form = CreateCalendar()
    return render(response, 'main/createCalendar.html', {'form': form})
