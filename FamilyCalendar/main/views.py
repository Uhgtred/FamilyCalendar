from django.shortcuts import render
from django.http import HttpResponse
from .models import Calendar, Appointment

# Create your views here.

def mainPage(response, name):
    appointment = Calendar.objects.get(name=name)
    items = appointment.item_set.all(id=1)
    return HttpResponse('<h1>%s</h1><br></br><p>%s</p>' % (appointment, str(items.name)))

