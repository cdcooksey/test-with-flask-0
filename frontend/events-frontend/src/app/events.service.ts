import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EventsService {
	private baseUrl = 'http://127.0.0.1:5000/api/v1';

  constructor(private http: HttpClient) { }

  getEvents(page: number): Observable<any> {
		return this.http.get(`${this.baseUrl}/events?page=${page}`);
  }
}
