from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Carlist
from .forms import ReviewForm
from django.urls import reverse

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


def RentalReview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
    else:
        form = ReviewForm()
        
    return render(request, 'rental_reviews.html', context={'form': form})


def Thankyou(request):
    return render(request, 'thank_you.html')