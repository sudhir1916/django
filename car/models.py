from django.db import models

# Create your models here.
class Carlist(models.Model):
    brand = models.CharField(max_length=50)
    year = models.IntegerField()


    def __str__(self):
        return self.brand