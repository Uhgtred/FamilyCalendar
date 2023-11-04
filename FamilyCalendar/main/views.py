from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Calendar, Appointment
from .forms import CreateCalendar, CreateAppointment


# Create your views here.

def home(response):
    return render(response, 'main/homeTemplate.html', {})


def calendarPage(response):
    appointmentList = Calendar.objects.get(id=1)
    return render(response, 'main/calendarTemplate.html', {'list': appointmentList, 'filter': True})


def createAppointment(response):
    if response.method == 'POST':
        form = CreateAppointment(response.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            persons = form.cleaned_data['persons']
            calendar = Appointment(name=name, description=description, date=date, involvedPersons=persons)
            calendar.save()
    else:
        form = CreateAppointment()
    return render(response, 'main/createAppointmentTemplate.html', {'form': form})


def createCalendar(response):
    if response.method == 'POST':
        form = CreateCalendar(response.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            calendar = Calendar(year=year)
            calendar.save()
        return HttpResponseRedirect("%i" %calendar.id)
    else:
        form = CreateCalendar()
    return render(response, 'main/createCalendarTemplate.html', {'form': form})