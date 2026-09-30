import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
  <h1>{{ dateTime | date:'dd/MM/yyyy HH:mm:ss' }}</h1>
  `
})
export class AppComponent {
  dateTime = new Date();
}