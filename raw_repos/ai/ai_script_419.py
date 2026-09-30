import requests
def get_average_temperature(city):
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=your_api_key'
    response = requests.get(api_url)
    data = response.json()
    temp = data['main']['temp']
    return temp - 273.15