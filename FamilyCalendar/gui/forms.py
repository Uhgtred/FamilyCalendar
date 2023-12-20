#!/usr/bin/env python3
# @author      Markus Kösters
import datetime

from django import forms


class CreateCalendar(forms.Form):
    """
    Form for receiving data from url.
    """
    # year in which the calendar is valid
    year = forms.IntegerField()


class CreateAppointment(forms.Form):
    """
    Form for receiving data from url.S
    """
    # name of the appointment.
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}), label='Name', max_length=50)
    # date on which the appointment occurs.
    date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-input'}), label='Datum')
    # end of appointment
    endDate = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-input'}), label='Ende des Termins', required=False)
    # persons who need to attend the appointment.
    persons = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}), label='Teilnehmer', max_length=100, required=False)
    # description of the appointment.
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input'}), label='Beschreibung', max_length=250, required=False)
