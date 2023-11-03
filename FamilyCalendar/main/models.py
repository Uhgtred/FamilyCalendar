import datetime

from django.db import models


class Calendar(models.Model):
    """
    Class for modeling the calendar.
    """
    year = models.IntegerField()

    def __str__(self):
        return self.year


class Appointment(models.Model):
    """
    Class defining the model of an appointment in the Calendar.
    """
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    dueDate = models.DateTimeField(datetime.date.today())
    involvedPersons = models.CharField(max_length=500)

    def __str__(self):
        return self.name


# class Task(models.Model, Appointment):
#     complete = models.BooleanField()
