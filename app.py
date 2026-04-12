import requests
from datetime import datetime

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = response.json()

print(f"Post ID: {data['id']}")
print(f"Title: {data['title']}")
print(f"Body: {data['body']}")
