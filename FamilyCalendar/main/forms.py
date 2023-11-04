#!/usr/bin/env python3
# @author      Markus Kösters

from django import forms


class CreateAppointment(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    date = forms.DateField(label='Date')
    persons = forms.CharField(label='Teilnehmer', max_length=100)
    description = forms.CharField(label='Beschreibung', max_length=250)


# class CreateTask(forms.Form, CreateAppointment):
#     complete = forms.BooleanField()


class CreateCalendar(forms.Form):
    year = forms.IntegerField()
