from operator import length_hint
from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    city_link = models.URLField(max_length=128, default='www.google.com')
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures') #if you delete an aiport, it will delete the flight
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    ticketprice = models.DecimalField(max_digits=6, decimal_places=2, default=100.00)
    MALE = "Male"
    FEMALE = "Female"
    PRIVATE = "Private"
    Choices = [
        ("male", MALE),
        ("female", FEMALE),
        ("private", PRIVATE)
    ]
    gender = models.CharField(max_length=8, choices=Choices, default="private", blank=True)
    #add seat numbers later 


    def __str__(self):
        return f"{self.first} {self.last}"