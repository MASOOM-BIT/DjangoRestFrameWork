import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Login } from './login';
@Injectable({
  providedIn: 'root'
})
export class Reservation {
  flightsUrl : string = 'http://127.0.0.1:8000/flightServices/findFlights/';
  singleFlightUrl : string = 'http://127.0.0.1:8000/flightServices/flights/';
  saveReservationUrl : string = 'http://127.0.0.1:8000/flightServices/saveReservation/';


  constructor(private http:HttpClient,private loginService:Login) { }
public getFlights(criteria):any{
  return this.http.post(this.flightsUrl,criteria,this.loginService.httpOptions);
}
}
