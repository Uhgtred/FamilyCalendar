from django.contrib import admin
from .models import Calendar, Appointment, Month

# Register your models here, to show up inside admin-panel.
admin.site.register(Calendar)
admin.site.register(Appointment)
admin.site.register(Month)
