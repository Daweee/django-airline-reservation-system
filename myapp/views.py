from django.shortcuts import render

from .models import BookedOneWay, BookedRoundTrip, OneWayFlight, RoundTripFlight
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin123':
            return redirect('http://localhost:8000/admin')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if username == 'mandawe' and password == 'mandawe':
                return redirect('http://localhost:8000/user')
            else:
                messages.error(request, 'User not found. Please try again.')
        else:
            messages.error(
                request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        getAllUser = User.objects.filter(username=username)
        getAllEmail = User.objects.filter(email=email)
        correctPass = 1
        correctUser = 1
        correctEmail = 1

        if len(password) < 6:
            messages.error(
                request, 'Password must be longer than 6 characters')
            correctPass = 0
            return redirect('http://localhost:8000/register/')

        if getAllUser:
            messages.error(request, 'Username already exist')
            correctUser = 0
            return redirect('http://localhost:8000/register/')

        if getAllEmail:
            messages.error(request, 'Email already Used')
            correctEmail = 0
            return redirect('http://localhost:8000/register/')

        if correctPass == 1 and correctUser == 1 and correctEmail == 1:
            newAccount = User.objects.create_user(
                username=username, email=email, password=password)
            newAccount.save()
            messages.success(request, 'User successfully Added')
            return redirect('http://localhost:8000/user/')

    return render(request, 'register.html')


def all_flights(request):
    one_way_flights = OneWayFlight.objects.all()
    round_trip_flights = RoundTripFlight.objects.all()
    return render(request, 'user.html', {'one_way_flights': one_way_flights, 'round_trip_flights': round_trip_flights})


def book_flights(request):
    if request.method == 'POST':
        flight_id = request.POST.get('id')
        flightType = request.POST.get('flightType')
        if flight_id and flightType:
            if flightType == 'One-Way':
                flight = OneWayFlight.objects.get(id=flight_id)
                booked_flight = BookedOneWay(flightType=flight.flightType,
                                             destination=flight.destination,
                                             departureDate=flight.departureDate,
                                             totalAmount=flight.totalAmount,
                                             )
                booked_flight.save()
            elif flightType == 'Round-Trip':
                flight = RoundTripFlight.objects.get(id=flight_id)
                booked_flight = BookedRoundTrip(flightType=flight.flightType,
                                                destination=flight.destination,
                                                departureDate=flight.departureDate,
                                                returnDate=flight.returnDate,
                                                totalAmount=flight.totalAmount,
                                                )
                booked_flight.save()
            messages.success(request, 'Flight Successfully Booked')
    return redirect(request.META.get('HTTP_REFERER'))


def confirmed_flights(request):
    booked_one_way = BookedOneWay.objects.all
    booked_round_trip = BookedRoundTrip.objects.all
    return render(request, 'flights.html', {'booked_one_way': booked_one_way, 'booked_round_trip': booked_round_trip})
