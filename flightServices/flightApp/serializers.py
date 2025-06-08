from rest_framework import serializers
from flightApp.models import Flight, Passanger, Reservation
import re

def isFlightNumberValid(flight_number):
    print('isFlightNumberValid')
    # if(re.match(r'^[A-Z]{2}\d{4}$', flight_number) is None):
    #     return False
    # return True
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [isFlightNumberValid]
    
    # def validate_flight_number(self, flight_number):
    #     print('validate_flight_number')
    #     if(re.match(r'^[A-Z]{2}\d{4}$', flight_number) is None):
    #         raise serializers.ValidationError("Flight number must be in the format 'XX1234' where 'XX' are uppercase letters and '1234' are digits.")
    # def validate(self, data):
    #     print('validate')
    #     print(data['flight_number'])
    #     return data

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passanger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'