from django.db import models


# Create your models here.

class Calendar(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    dueDate = models.DateTimeField()  # dunno if this is correct!
    involvedPersons = models.CharField(max_length=500)

    def __str__(self):
        return self.description
