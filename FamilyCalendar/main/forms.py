#!/usr/bin/env python3
# @author      Markus Kösters

from django import forms


class CreateCalendar(forms.Form):
    """
    Form for receiving data from url.
    """
    # year in which the calendar is valid
    year = forms.IntegerField()


class CreateAppointment(forms.Form):
    """
    Form for receiving data from url.
    """
    # name of the appointment.
    name = forms.CharField(label='Name', max_length=50)
    # date on which the appointment occurs.
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), label='Datum', input_formats=['%d.%m.%Y'])
    # persons who need to attend the appointment.
    persons = forms.CharField(label='Teilnehmer', max_length=100)
    # description of the appointment.
    description = forms.CharField(label='Beschreibung', max_length=250)
