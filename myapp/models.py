from django.db import models
from django.contrib.auth.models import User

# class models


class BookedOneWay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flightType = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departureDate = models.DateField()
    totalAmount = models.CharField(max_length=200)


class BookedRoundTrip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flightType = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departureDate = models.DateField()
    returnDate = models.DateField()
    totalAmount = models.CharField(max_length=200)


class RoundTripFlight(models.Model):
    flightType = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departureDate = models.DateField()
    returnDate = models.DateField()
    totalAmount = models.CharField(max_length=200)


class OneWayFlight(models.Model):
    flightType = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departureDate = models.DateField()
    totalAmount = models.CharField(max_length=200)
