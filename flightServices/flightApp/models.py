from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    operatingAirline = models.CharField(max_length=100)
    departureCity = models.CharField(max_length=100)
    arrivalCity = models.CharField(max_length=50)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

class Passanger(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passanger = models.OneToOneField(Passanger, on_delete=models.CASCADE)