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
  getEventDetails(eventId: number) {
    return this.http.get(`${this.baseUrl}/events/${eventId}`);
  }

  // TODO Consider better name for this as all it does on the backend is
  // increment the participant_count.
  updateEvent(eventId: number) {
    let payload = {}; // We have no data to send but must send something
    return this.http.put(`${this.baseUrl}/events/${eventId}`, payload);
  }
}
