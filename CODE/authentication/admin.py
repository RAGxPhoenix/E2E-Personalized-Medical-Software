
# Register your models here.
# admin.py in your authentication app

from django.contrib import admin
from .models import Patient, Doctor,Feedback

# Register your custom user models with the admin site
admin.site.register(Patient)

admin.site.register(Doctor)

admin.site.register(Feedback)
