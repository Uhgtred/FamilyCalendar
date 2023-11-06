from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import CreateCalendar, CreateAppointment
from .models import Calendar


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
        And all assigned Appointments.
        :param response: Response passed from the form.
        :param year: Year in which the shown calendar is valid.
        :return: Render of the requested calendar.
        """
        calendar = Calendar.objects.get(year=year)
        return render(response, 'main/calendar.html', {'list': calendar})

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
        form = CreateCalendar(response.POST)
        if not response.method == 'POST':
            form = CreateCalendar()
        if form.is_valid():
            year = form.cleaned_data['year']
            calendar = Calendar(year=year)
            calendar.save()
            return HttpResponseRedirect("%i" % calendar.id)
        return render(response, 'main/createCalendar.html', {'form': form})


class Appointments:
    """
    Class for defining views related to Appointments.
    """

    @staticmethod
    def createAppointment(response):
        """
        Method for creating a new appointment.
        :param response: Response passed from the form.
        :return: Render of the newly created appointment.
        """
        form = CreateAppointment(response.POST)
        if not response.method == 'POST':
            form = CreateAppointment()
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            persons = form.cleaned_data['persons']
            calendar = Calendar.objects.get(year=date.year)
            calendar.appointment_set.create(name=name, description=description, date=[date.day, date.month], persons=persons)
            return render(response, 'main/calendar.html', {'list': calendar})
        return render(response, 'main/createAppointment.html', {'form': form})

    @staticmethod
    def appointment(response, appointmentID: int):
        """
        Method for viewing the details of a specific appointment.
        :param response: Response passed from the form.
        :param appointmentID: Unique ID of the appointment that will be shown.
        :return: Render of the appointment that will be shown.
        """
        calendars = Calendar.objects.all()
        for calendar in calendars:
            print(f'CALENDAR!!! {calendar.appointment_set(id=appointmentID)}')
            try:
                calendar.appointment_set.get(id=appointmentID)
            except:
                pass
        return render(response, 'main/appointment.html', {'list': calendar})
