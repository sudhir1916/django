from django.urls import path
from . import views


urlpatterns =[
    path('home/', views.HomeView.as_view(), name='home'),
    path('thank-you/', views.ThankyouView.as_view(), name="Thank-you"),
    path('contact/', views.ContactFormView.as_view(), name="contact")
]