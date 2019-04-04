#!/usr/bin/env python3

import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dr.settings')

import django
django.setup()

from faker import Faker

from portal.models import Event, PersonStatus


Event.objects.all().delete()
PersonStatus.objects.all().delete()

fire_event = Event(name='fire_sale')
fire_event.save()

missing_status = PersonStatus(name='missing')
missing_status.save()

safe_status = PersonStatus(name='safe')
safe_status.save()

# to do: create 30 Person objects using Faker

def fake_name_maker():
	fake = Faker()
	for _ in range(30):
	    fake.name()

# denerate the whole object with all the values! put this into the database the id autoincremenets. 
# now turn this into data in the database!...?

class Personobject():
	fake = Faker()
	first_name = fake.first_name()
	last_name = fake.last_name()













