#!/usr/bin/env python3
# @author      Markus Kösters

from django import forms


class CreateCalendar(forms.Form):
    year = forms.IntegerField()


class CreateAppointment(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), label='Datum', input_formats=['%d.%m.%Y'])
    persons = forms.CharField(label='Teilnehmer', max_length=100)
    description = forms.CharField(label='Beschreibung', max_length=250)
