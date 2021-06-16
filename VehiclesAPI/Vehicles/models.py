from django.db import models
from django.db.models.base import Model

# Create your models here.
class BaseVehicle(models.Model):
    Make = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    Year = models.IntegerField()
    ServiceInterval = models.CharField(max_length=255)
    NextService = models.CharField(max_length=255)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.Make + '-' + self.Model
        


class Car( BaseVehicle ):
    Seats = models.IntegerField()
    Color = models.CharField(max_length=255)
    VIN = models.CharField(max_length=255)
    CurrentMileage = models.IntegerField()

class Truck( BaseVehicle ):
    Seats = models.IntegerField()
    BedLength = models.CharField(max_length=255)
    Color = models.CharField(max_length=255)
    VIN = models.CharField(max_length=255)
    CurrentMileage = models.IntegerField()

class Boat( BaseVehicle ):
    Length = models.IntegerField()
    Width = models.CharField(max_length=255)
    HIN = models.CharField(max_length=255)
    CurrentHours = models.IntegerField()
