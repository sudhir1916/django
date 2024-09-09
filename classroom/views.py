from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from classroom.forms import ContactForm


# Create your views here.

# def home(request):
#     return HttpResponse('Classroom')


class HomeView(TemplateView):
    template_name = 'home.html'


class ThankyouView(TemplateView):
    template_name = 'thank-you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact-form.html'

    success_url = "/classroom/thank-you/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)