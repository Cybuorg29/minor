import requests

# Make the API call
url = "https://dummyapi.io/data/api/user"
response = requests.get(url)

# Fetch the information
if response.status_code == 200:
    data = response.json()
    username = data['username']
    email = data['email']
    # Print the obtained info
    print(f'Username: {username}, Email: {email}')