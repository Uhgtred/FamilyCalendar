from django.contrib import admin

from FamilyCalendar.gui.models import Calendar, Appointment, Month, Day

# Register your models here.
admin.site.register(Calendar)
admin.site.register(Appointment)
admin.site.register(Month)
admin.site.register(Day)
