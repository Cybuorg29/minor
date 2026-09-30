import requests

r = requests.get('http://www.example.com/page')

if r.status_code == 200:
    data = r.text
    names = re.findall(r'<span class="name">(.*?)</span>', data)
    emails = re.findall(r'<span class="email">(.*?)</span>', data)