import requests

url = "https://api.example.com/v1/search"

response = requests.get(url)
data = response.json()
print(data)