from django.contrib import admin
from .models import Person


# to do: register models for Admin app to use
admin.site.register(Person)