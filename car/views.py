from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Carlist

# Create your views here.

def CarList(request):
    cars = Carlist.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'list.html', context=context)


def AddCar(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        year = int(request.POST.get('year'))
        carQuery = Carlist.objects.create(brand=brand, year=year)
        if carQuery:
            return redirect('car-list')
        return HttpResponse('Invalid request')
    return render(request, 'add.html')



def CarDelete(request, id):
    car = Carlist.objects.get(id=id).delete()
    if car:
        return redirect('car-list')
