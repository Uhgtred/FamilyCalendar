from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateCalendar, CreateAppointment
from .models import Calendar


# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})


class Calendars:
    """
    Class for defining views related to calendar-pages.
    """

    @staticmethod
    def calendarPage(response, year: int):
        """
        Method for viewing a calendar-page of a specified year.
        :param response: Response passed from the form.
        :param year: Year in which the shown calendar is valid.
        :return: Render of the requested calendar.
        """
        calendar = Calendar.objects.get(year=year)
        return render(response, 'main/calendar.html', {'list': calendar, 'filter': True})

    @staticmethod
    def allCalendars(response):
        """
        Method for showing an overview of all existing calendars.
        :param response: Response passed from the form.
        :return: Render of all calendars in the DataBase.
        """
        calendars = Calendar.objects.all()
        return render(response, 'main/allCalendars.html', {'list': calendars})

    @staticmethod
    def createCalendar(response):
        """
        Method for creating a new calendar.
        :param response: Response passed from the form.
        :return: Render of the calendar that has just been created.
        """
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


class Appointments:
    """
    Class for defining views related to Appointments.
    """

    @staticmethod
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
