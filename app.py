import requests

# 1. הכתובת של ה-API (תחנת החלל)
url = "http://api.open-notify.org/iss-now.json"

# 2. שליחת הבקשה
response = requests.get(url)

# 3. בדיקה אם קיבלנו 200 (כמו שהמרצה אמר)
if response.status_code == 200:
    data = response.json() # הופך את הטקסט למילון של פייתון
    print("Success!")
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(f"The type is: {type(response)}")
    print(f"The response object is: {response}")