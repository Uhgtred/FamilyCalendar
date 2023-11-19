from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import calendar

from .forms import CreateCalendar, CreateAppointment
from .models import Calendar, Appointment, Month, Day


def home(response):
    return render(response, 'main/home.html', {})


class Calendars:
    """
    Class for defining views related to calendar-pages.
    """

    @staticmethod
    def calendarPage(response, year: int, month: int):
        """
        Method for viewing a calendar-page of a specified year.
        And all assigned Appointments.
        :param month: Integer-value for the month of which the calendar-Page will be shown.
        :param response: Response passed from the form.
        :param year: Year in which the shown calendar is valid.
        :return: Render of the requested calendar.
        """
        firstDay = calendar.monthrange(year, month)[0]
        days = Day.objects.get(year=year, month=month)
        numberOfDaysInPreviousMonth = calendar.monthrange(year, month - 1)[1]
        print(firstDay, days)
        # Making the days of the last month visible back until monday.
        # This could potentially go to an own class later on, for modularity.
        daysBeforeList = [i for i in reversed(range(numberOfDaysInPreviousMonth, (numberOfDaysInPreviousMonth - firstDay), -1))]
        print(daysBeforeList)
        dayList = daysBeforeList + days
        print(dayList)
        year = Calendar.objects.get(year=year)
        month = Month.objects.get(year=year, month=month)
        monthName = month.name
        return render(response, 'main/calendar.html', {'year': year, 'month': monthName, 'numberOfDays': dayList})

    @staticmethod
    def allCalendars(response):
        """
        Method for showing an overview of all existing calendars.
        :param response: Response passed from the form.
        :return: Render of all calendars in the DataBase.
        """
        calendars = Calendar.objects.all()
        return render(response, 'main/allCalendars.html', {'list': calendars})

    @classmethod
    def createCalendar(cls, response):
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
            calendar_ = Calendar(year=year)
            calendar_.save()
            cls.createMonths(calendar_)
            calendar_.save()
            cls.createDays(calendar_)
            return HttpResponseRedirect("%i" % calendar_.id)
        return render(response, 'main/createCalendar.html', {'form': form})

    @classmethod
    def createMonths(cls, calendar_) -> None:
        for month in range(1, 13):
            calendar_.month_set.create(month=month, name=calendar.month_name[month])
        # calendar_.save()

    @classmethod
    def createDays(cls, calendar_):
        months = calendar_.month_set.all()
        for month in months:
            for day in range(1, calendar.monthrange(year=calendar_.year, month=month.month)[1]):
                Day.objects.create(day=day, month=month)
            calendar_.save()


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
            month = Month.objects.get(month=date.month)
            month.appointment_set.create(name=name, description=description, date=date, persons=persons)
            return render(response, 'main/calendar.html', {'list': calendar})
        return render(response, 'main/createAppointment.html', {'form': form})

    @staticmethod
    def appointment(response, name: str):
        """
        Method for viewing the details of a specific appointment.
        :param name:
        :param response: Response passed from the form.
        :return: Render of the appointment that will be shown.
        """
        appointments = Appointment.objects.all()
        relevantAppointments: list = []
        for appointment in appointments:
            if appointment.name == name:
                relevantAppointments.append(appointment)
        return render(response, 'main/appointment.html', {'list': relevantAppointments, 'name': name})
