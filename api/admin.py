from django.contrib import admin

# Register your models here.

from .models import Person, Vehicle
admin.site.register(Person)
admin.site.register(Vehicle)
