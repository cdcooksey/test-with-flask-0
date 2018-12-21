import { Component, OnInit } from '@angular/core';
import { EventsService } from './events.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {
  title    = 'Events';
  subtitle = 'DNC Code Challenge';
  page:   number;
  events: Array<any>; // TODO Create Event model and cast as Array<Event>
  selectedEvent: any; // TODO Use Event model

  constructor(private eventsService: EventsService) {
    this.page = 0;
    this.events = [];
  }

  ngOnInit() {
    return this.getEvents();
  }

  getEvents(): void {
    this.events = []; // TODO Use redux / reducer to cut down on API calls.
    this.eventsService
      .getEvents(this.page)
      .subscribe(events => this.addEvents(events));
  }

  // TODO Cast events as Array<Event>
  addEvents(events: Array<any>) {
    for(let event of events) {
      this.events.push(event);
    }
  }

  // TODO Cast event as Event model
  onSelect(event: any) {
    this.eventsService
      .getEventDetails(event.id)
      .subscribe(event => this.selectedEvent = event);
  }

  closeDetails() {
    this.selectedEvent = false;
  }

  previousPage() {
    if(this.page > 0) {
      this.page--;
      this.getEvents();
    }
    return false;
  }

  nextPage() {
    this.page++;
    this.getEvents();
  }

  attend(event: any) {
    console.log(event);
  }

  showDetails() {
    if(this.selectedEvent) {
      return true;
    }
    return false;
  }
}
