"""
URL configuration for flightServices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from flightApp import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
# Importing the necessary modules for the Django project.
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('flights', views.FlightViewSet)
router.register('passengers', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('flightServices/', include(router.urls)),
    # path('flightServices/findFlights/', views.find_flight, name='find_flight'),
    # path('flightServices/saveReservation/', views.save_reservation, name='save_reservation'),
    path('api-token-auth/', obtain_auth_token , name='api-token-auth'),

]
