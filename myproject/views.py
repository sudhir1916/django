from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Patient

# Create your views here.

def index(request):
    return HttpResponse("Hello, This is the first class of django")


def simple_view(request):
    return render(request, 'example.html')


def varialbe_view(request):
    my_var = {
        'name': 'John',
        'age': 30,
        'location' : 'india'

    }
    return render(request, 'variable.html', context=my_var)


def PatientView(request):
    patient = Patient.objects.all()
    context = {
        'patient':patient
    }
    return render(request, 'patient.html', context=context)