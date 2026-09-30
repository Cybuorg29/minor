import { Component } from '@angular/core';

@Component({
  selector: 'app-timer',
  template: `
  {{ counter }}
  `
})
export class TimerComponent {
  counter = 0;

  constructor() {
    setInterval(() => {
      this.counter++;
    }, 1000);
  }
}