from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.CarList, name='car-list'),
    path('add/', views.AddCar, name='add-car'),
    path('delete/<int:id>/', views.CarDelete, name='delete'),
]
