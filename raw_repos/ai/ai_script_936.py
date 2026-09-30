import requests

data = {
 "id": "123456",
 "name": "John Doe"
}

url = "http://example.com/update-user-name"

response = requests.post(url, json=data)