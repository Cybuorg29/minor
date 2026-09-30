import { Directive, ElementRef, HostListener } from '@angular/core';

@Directive({
 selector: '[appNotifyOnChange]'
})
export class NotifyOnChangeDirective {
 constructor(private el: ElementRef) { }

@HostListener('input', ['$event'])
onChange(event) {
 alert('Value changed to: ' + event.target.value);
}
}