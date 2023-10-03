from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def mainPage(response):
    return HttpResponse('<h1>Family-Calendar</h1>')
