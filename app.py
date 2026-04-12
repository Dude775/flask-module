import requests
from datetime import datetime

response = requests.get("http://api.open-notify.org/iss-now.json")

data = response.json()

print(data["iss_position"])
ts = data["timestamp"]
TIME = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print(f"Current ISS location at {TIME} is LAT: {data['iss_position']['latitude']}, LON: {data['iss_position']['longitude']}")
