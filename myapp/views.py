from django.shortcuts import render

from .models import BookedOneWay, BookedRoundTrip, OneWayFlight, RoundTripFlight, Flight
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect

# Create your views here.


def login_view(request):
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
            authenticated_user = authenticate(
                request, username=username, password=password)
            if authenticated_user is not None:
                auth_login(request, authenticated_user)
                messages.success(request, 'User successfully added')
                return redirect('http://localhost:8000/user/')

    return render(request, 'register.html')


# def admin_page(request):
#     if not request.user.is_authenticated or not request.user.is_staff:
#         return redirect('userPage')
#     return render(request, 'admin.html')


def add_one_way_flight(request):
    if request.method == 'POST':
        destination = request.POST['destination']
        departure_date = request.POST['departure_date']
        price = request.POST['price']

        OneWayFlight.objects.create(
            flightType='One-Way',
            destination=destination,
            departureDate=departure_date,
            totalAmount=price
        )

        messages.success(request, 'One-Way Flight added successfully.')

    one_way_flights = OneWayFlight.objects.all()
    round_trip_flights = RoundTripFlight.objects.all()
    return render(request, 'user.html', {'one_way_flights': one_way_flights, 'round_trip_flights': round_trip_flights})


def add_round_trip_flight(request):
    if request.method == 'POST':
        destination = request.POST['destination']
        departure_date = request.POST['departure_date']
        return_date = request.POST['return_date']
        price = request.POST['price']

        RoundTripFlight.objects.create(
            flightType='Round-Trip',
            destination=destination,
            departureDate=departure_date,
            returnDate=return_date,
            totalAmount=price
        )

        messages.success(request, 'Round-Trip Flight added successfully.')

    one_way_flights = OneWayFlight.objects.all()
    round_trip_flights = RoundTripFlight.objects.all()
    return render(request, 'user.html', {'one_way_flights': one_way_flights, 'round_trip_flights': round_trip_flights})


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
