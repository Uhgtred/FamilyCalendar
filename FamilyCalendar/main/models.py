from django.db import models


class Calendar(models.Model):
    """
    Class for modeling the calendar.
    """
    year = models.IntegerField()

    def __str__(self):
        # Showing calendar-table in admin-panel with the valid year as name.
        return str(self.year)


class Month(models.Model):
    # making months a subitem of calendar
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    month = models.IntegerField()
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Day(models.Model):
    """
    Class for modeling a day inside the calendar.
    """
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    day = models.IntegerField()

    def __str__(self):
        return str(self.day)


class Appointment(models.Model):
    """
    Class defining the model of an appointment inside the Calendar.
    """
    # making appointments be a subitem of month
    month = models.ForeignKey(Day, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    date = models.DateTimeField()
    endDate = models.DateTimeField()
    persons = models.CharField(max_length=100)

    def __str__(self):
        # Showing appointments in admin-table with their name.
        return self.name
