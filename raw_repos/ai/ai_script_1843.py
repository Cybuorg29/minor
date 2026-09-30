using System;
 
public class EventListener
{
     public delegate void EventListenerHandler(object sender, EventArgs e);
     public event EventListenerHandler SomeEvent;
 
     public void OnSomeEvent(EventArgs e)
     {
          if (SomeEvent != null)
          {
               SomeEvent(this, e);
          }
     }
}