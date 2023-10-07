from django.shortcuts import render
from django.http import HttpResponse
from .models import Calendar, Appointment


# Create your views here.

def home(response):
    return render(response, 'main/homeTemplate.html', {})


def calendarPage(response):
    appointmentsList = Calendar.objects.get(id=1)
    return render(response, 'main/calendarTemplate.html', {'list': appointmentsList, 'filter': True})
