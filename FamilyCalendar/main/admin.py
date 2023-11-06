from django.contrib import admin
from .models import Calendar, Appointment

# Register your models here, to show up inside admin-panel.
admin.site.register(Calendar)
admin.site.register(Appointment)
