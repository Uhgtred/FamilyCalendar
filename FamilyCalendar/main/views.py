from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import calendar

from .forms import CreateCalendar, CreateAppointment
from .models import Calendar, Appointment, Month


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
        firstDay, numberOfDays = calendar.monthrange(year, month)
        numberOfDaysInPreviousMonth = calendar.monthrange(year, month - 1)[1]
        print(firstDay, numberOfDays)
        # Making the days of the last month visible back until monday.
        # This could potentially go to an own class later on, for modularity.
        daysBeforeList = [i for i in reversed(range(numberOfDaysInPreviousMonth, (numberOfDaysInPreviousMonth - firstDay), -1))]
        print(daysBeforeList)
        dayList = daysBeforeList + [i for i in range(1, numberOfDays + 1)]
        print(dayList)
        year = Calendar.objects.get(year=year)
        monthName = Calendars.getMonthNameByNumber(month)
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
            calendar_ = Calendar(year=year)
            # calendar_.save()
            for month in range(1, 13):
                """TODO: this needs to be it's own method!"""
                """Need to use forms to get this running correctly!!!"""
                """https://forum.djangoproject.com/t/valueerror-needs-to-have-a-value-for-field-id-before-this-many-to-many-relationship-can-be-used/1808
                This forum-thread can possibly help on solving this issue
                needs to have a value for field "id" before this relationship can be used. --> Error-message that has been thrown"""
                calendarMonth = calendar_.month_set.create(month=month, name=calendar.month(year, month), firstDay=calendar.monthrange(year, month))
                # calendar_.save()
                numberOfDays = calendar.monthrange(year, month)[1]
                [calendarMonth.day_set.create(day=i) for i in range(numberOfDays)]
            calendar_.save()
            return HttpResponseRedirect("%i" % calendar_.id)
        return render(response, 'main/createCalendar.html', {'form': form})

    @staticmethod
    def getMonthNameByNumber(month: int) -> str:
        """
        Returning a name (str) of the month that fits to the integer that has been passed.
        :param month: integer representing a month.
        :return: string representing a month.
        """
        match month:
            case 1:
                return 'Januar'
            case 2:
                return 'Februar'
            case 3:
                return 'Maerz'
            case 4:
                return 'April'
            case 5:
                return 'Mai'
            case 6:
                return 'Juni'
            case 7:
                return 'Juli'
            case 8:
                return 'August'
            case 9:
                return 'September'
            case 10:
                return 'Oktober'
            case 11:
                return 'November'
            case 12:
                return 'Dezember'


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
