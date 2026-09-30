public class TemperatureReading {
  private Date date;
  private String location;
  private int temperature;

  public TemperatureReading(Date date, String location, int temperature) {
    this.date = date;
    this.location = location;
    this.temperature = temperature;
  }

  public Date getDate() {
    return date;
  }

  public String getLocation() {
    return location;
  }

  public int getTemperature() {
    return temperature;
  }
}