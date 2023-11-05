from django.contrib import admin
from .models import Calendar, Appointment

# Register your models here.
admin.site.register(Calendar)
admin.site.register(Appointment)