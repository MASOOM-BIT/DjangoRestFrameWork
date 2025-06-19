import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, tap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  public httpOptions: any;

  constructor(private http: HttpClient) {
    this.httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    };
  }

  public login(): Observable<{ token: string }> {
    const user = {
      username: 'admin',
      password: 'admin'
    };

    return this.http.post<{ token: string }>(
      'http://localhost:8080/api-token-auth/',
      JSON.stringify(user),
      this.httpOptions
    ).pipe(
      tap(response => {
        this.httpOptions = {
          headers: new HttpHeaders({
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + response.token
          })
        };
        // Optionally: Store token in localStorage/sessionStorage
        localStorage.setItem('auth_token', response.token);
      })
    );
  }
}
