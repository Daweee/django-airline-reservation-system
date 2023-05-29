"""
URL configuration for airline_reservation_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminpage/', TemplateView.as_view(template_name='admin.html'),
         name='adminPage'),
    path('add-one-way-flight/', views.add_one_way_flight,
         name='add_one_way_flight'),
    path('add-round-trip-flight/', views.add_round_trip_flight,
         name='add_round_trip_flight'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('register/', views.register, name="registerUser"),
    path('login/', views.login_view, name="loginUser"),
    path('logout/', views.logout, name="logoutUser"),
    path('user/', views.all_flights, name='all_flights'),
    path('book/', views.book_flights, name='book'),
    path('confirm/', views.confirmed_flights, name='confirm'),
]
