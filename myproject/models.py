from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinLengthValidator(0), MaxLengthValidator(100)])
    address = models.TextField(max_length=100)
    bp = models.IntegerField(default=80, validators=[MinLengthValidator(80), MaxLengthValidator(120)])

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}, BP : {self.bp}"
    

