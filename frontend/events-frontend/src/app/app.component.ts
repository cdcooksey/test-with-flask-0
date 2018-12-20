import { Component, OnInit } from '@angular/core';
import { EventsService } from './events.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {
  title = 'Events';
  subtitle = 'DNC Code Challenge';
  page: number;
  events: Array<any>; // TODO Create Event model and cast as Array<Event>

  constructor(private eventsService: EventsService) {
		this.page = 0;
		this.events = [];
	}

	ngOnInit() {
		return this.getEvents();
	}

  getEvents(): void {
    this.eventsService
      .getEvents(this.page)
      .subscribe(events => this.addEvents(events));
  }

  addEvents(events: Array<any>) {
    for(let event of events) {
      this.events.push(event);
    }
  }

  onSelect() {
    return 'do nothing';
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
}
