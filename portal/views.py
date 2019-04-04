from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .models import Person

from .models import PersonStatus,Person
from .forms import NameForm


def index(request):
	return render(request, 'portal/index.html')


def add_person(request):
    form = NameForm()
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data['first_name']
            last_name = data['first_name']
            new_person= Person(first_name=first_name, last_name=last_name)
            new_person.save()
            
        return redirect('portal:index')
    return render(request, 'portal/add_person.html', {'form':form})


def show_person(request):
    person = Person.objects.all()
    context={'person':person}
    print(context)
    return render(request , 'portal/show_person.html', context)
    

def show_safe_persons(request):
    persons = None # ... change this line!
    return render(request, 'portal/show_persons.html', {
        'title': 'Persons marked as Safe',
        'main_heading': 'Persons Marked as Safe',
        'persons': persons })


def search_person(request):
    context = None
    if request.method != 'POST':
        return redirect('portal:index')

    text = request.POST.get('search', '')
    # results = Person.objects.filter(
    #     Q(first_name__icontains=text) |
    #     Q(last_name__icontains=text) |
    #     Q(other_name__icontains=text) |
    #     Q(description__icontains=text))

    # to do: render a page with the results.
