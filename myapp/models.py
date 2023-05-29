from django.db import models

# class models


class BookedOneWay(models.Model):
    flightType = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departureDate = models.DateField()
    totalAmount = models.CharField(max_length=200)


class BookedRoundTrip(models.Model):
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


class Flight(models.Model):
    flightType = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departureDate = models.DateField()
    returnDate = models.DateTimeField(max_length=200, null=True, blank=True)
    totalAmount = models.CharField(max_length=200)
