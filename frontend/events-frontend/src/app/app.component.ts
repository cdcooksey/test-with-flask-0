import { Component, OnInit } from '@angular/core';
import { EventsService } from './events.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {
  title = 'DNC Events Challenge';

  constructor(private eventsService: EventsService) { }

	ngOnInit() {
		return this.getEvents();
	}
	getEvents(): void {
		this.eventsService.getEvents().subscribe();
	}
}