from django.contrib import admin

# Register your models here.

from .models import Person, Vehicle, Schedule
admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(Schedule)
