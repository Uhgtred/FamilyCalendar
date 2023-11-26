from datetime import datetime

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
    def calendarPage(response, year: int, month: int) -> render:
        """
        Method for viewing a calendar-page of a specified year.
        And all assigned Appointments.
        :param month: Integer-value for the month of which the calendar-Page will be shown.
        :param response: Response passed from the form.
        :param year: Year in which the shown calendar is valid.
        :return: Render of the requested calendar.
        """
        firstDay = calendar.monthrange(year, month)[0]
        yearInstance = Calendar.objects.get(year=year)
        monthInstance = yearInstance.month_set.get(month=month)
        days = monthInstance.day_set.all()
        appointmentDict = {}
        for day in days:
            appointmentDict[str(day.day + 1)] = [(appointment.name, appointment.date, appointment.id) for appointment in day.appointment_set.all()]
        numberOfDaysInPreviousMonth = calendar.monthrange(year, month - 1)[1]
        # Making the days of the last month visible back until monday.
        daysBeforeList = [i for i in reversed(range(numberOfDaysInPreviousMonth, (numberOfDaysInPreviousMonth - firstDay), -1))]
        monthName = monthInstance.name
        return render(response, 'main/calendar.html', {'year': year, 'month': monthName, 'appointmentDict': appointmentDict, 'listOfLastMonth': daysBeforeList})

    @staticmethod
    def allCalendars(response) -> render:
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
            # Returning if calendar already exists
            # TODO: Make a Popup that informs user about existing calender
            try:
                Calendar.objects.get(year=year)
                return render(response, 'main/createCalendar.html', {'form': form})
            except Calendar.DoesNotExist:
                # TODO: make a loading-screen or since it takes quiet a while to create a new calendar
                print('Creating new Calendar')
            calendar_ = Calendar(year=year)
            calendar_.save()
            cls.createMonths(calendar_)
            cls.createDays(calendar_)
            return render(response, 'main/createCalendar.html') # TODO: direct to some page that informs about success of creating a new calendar
        return render(response, 'main/createCalendar.html', {'form': form})

    @classmethod
    def createMonths(cls, calendar_) -> None:
        for month in range(1, 13):
            calendar_.month_set.create(month=month, name=calendar.month_name[month])
        calendar_.save()

    @classmethod
    def createDays(cls, calendar_):
        months = calendar_.month_set.all()
        for month in months:
            for day in range(calendar.monthrange(year=calendar_.year, month=month.month)[1]):
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
            endDate = form.cleaned_data['endDate']
            yearInstance = Calendar.objects.get(year=date.year)
            monthInstance = yearInstance.month_set.get(month=date.month)
            day = monthInstance.day_set.get(day=date.day - 1)
            day.appointment_set.create(name=name, description=description, date=date, persons=persons, endDate=endDate)
            return Calendars.calendarPage(response, date.year, date.month)
        return render(response, 'main/createAppointment.html', {'form': form})

    @staticmethod
    def appointment(response, id: int) -> render:
        """
        Method for viewing the details of a specific appointment.
        :param id: Id that is used for identifying an appointment.
        :param response: Response passed from the form.
        :return: Render of the appointment that will be shown.
        """
        appointment = Appointment.objects.get(id=id)
        return render(response, 'main/appointment.html', {'appointment': appointment, 'name': appointment.name})
