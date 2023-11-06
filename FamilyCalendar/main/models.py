import datetime

from django.core.validators import validate_comma_separated_integer_list
from django.db import models


class Calendar(models.Model):
    """
    Class for modeling the calendar.
    """
    year = models.IntegerField()

    def __str__(self):
        # Showing calendar-table in admin-panel with the valid year as name.
        return str(self.year)


class Appointment(models.Model):
    """
    Class defining the model of an appointment inside the Calendar.
    """
    # making appointments be a subitem of calendars
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique_for_year=True)
    description = models.CharField(max_length=250)
    # date = models.CharField(validators=[validate_comma_separated_integer_list], max_length=10)
    date = models.DateField()
    date.input_formats = ['%d.%m.%Y']
    persons = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Task(models.Model, Appointment):
#     complete = models.BooleanField()
