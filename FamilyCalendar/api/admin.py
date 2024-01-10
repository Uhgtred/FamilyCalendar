from .models import Calendar, Appointment, Month, Day
from django.contrib import admin

# Register your models here.
admin.site.register(Calendar)
admin.site.register(Appointment)
admin.site.register(Month)
admin.site.register(Day)
