import requests

url = "https://www.google.com"
response = requests.post(url)

print(response.content)