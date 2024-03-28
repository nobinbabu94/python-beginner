from django.contrib import admin
from . models import departments, doctors, bookings
# Register your models here.

admin.site.register(departments),
admin.site.register(doctors) 
admin.site.register(bookings)