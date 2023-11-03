#!/usr/bin/env python3
# @author      Markus Kösters

from django import forms


class CreateAppointment(forms.Form):
    name = forms.CharField(label="Name", max_length=50)


# class CreateTask(forms.Form, CreateAppointment):
#     complete = forms.BooleanField()


class CreateCalendar(forms.Form):
    year = forms.IntegerField()
