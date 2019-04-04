from django.urls import path

from . import views

app_name = 'portal'
urlpatterns = [
	path('', views.index, name='index'),
	path('people', views.show_person, name='people'),
	path('addpeople', views.add_person , name='addpeople')
    # to do: add more paths...
]