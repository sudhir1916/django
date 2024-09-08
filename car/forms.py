from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     name = forms.CharField(max_length = 100, label='Name')
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Add your review here', max_length=100)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

        labels ={
            'name': 'Your Name',
            'email': 'Your Email',
            'review': 'Your Review',
        }

        error_messages ={
            'review':{
                'max_value': 'Please add the value less than or equal to 5',
                'min_value' : 'Please add the correct value'
            }
        }