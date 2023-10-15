#!/usr/bin/env python3
# @author      Markus Kösters

from django import forms


class CreateAppointment(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField()


class CreateCalendar(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField()
