import { Component } from '@angular/core';

@Component({
 selector: 'form-input',
 template: `
 <form>
  <input type="text" id="textInput" />
  <button type="submit">Submit</button>
 </form>
 `
})
export class FormInput {

}