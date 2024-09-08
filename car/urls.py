from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.CarList, name='car-list'),
    path('add/', views.AddCar, name='add-car'),
    path('delete/<int:id>/', views.CarDelete, name='delete'),
    path('rental-review/', views.RentalReview, name="rental-review"),
    path('thank-you/', views.Thankyou, name="thank-you")
]
