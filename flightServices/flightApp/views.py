from django.shortcuts import render
from flightApp.models import Flight, Passanger, Reservation
from flightApp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(['POST'])
def find_flight(request):
    flights = Flight.objects.filter(
        departureCity=request.GET.get('departureCity'),
        arrivalCity=request.GET.get('arrivalCity'),
        dateOfDeparture=request.GET.get('dateOfDeparture')
    )
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])
    passanger = Passanger()
    passanger.firstName = request.data['firstName']
    passanger.lastName = request.data['lastName']
    passanger.middleName = request.data['middleName']
    passanger.email = request.data['email']
    passanger.phone = request.data['phone']
    passanger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passanger = passanger
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)






class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passanger.objects.all()
    serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer