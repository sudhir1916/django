from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Carlist(models.Model):
    brand = models.CharField(max_length=50)
    year = models.IntegerField()


    def __str__(self):
        return self.brand
    
class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # Use MinValueValidator and MaxValueValidator

    def __str__(self):
        return self.name