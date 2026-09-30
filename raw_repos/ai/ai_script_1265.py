import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-user-info',
  template: `
    <div>
      <p>ID: {{ user.id }}</p>
      <p>Name: {{ user.name }}</p>
      <p>Age: {{ user.age }}</p>
      <p>Email: {{ user.email }}</p>
    </div>
  `
})
export class UserInfoComponent implements OnInit {

  user = {
    id: 1,
    name: 'Bob',
    age: 23,
    email: 'bob@example.com'
  };

  constructor() { }

  ngOnInit() {
  }

}