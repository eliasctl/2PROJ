import requests

url = "http://localhost:3000/displayList/admin3"

response = requests.get(url)
print(response.status_code)
print(response.text)
print(response.json())

listResult = response.json()
print(listResult[0]['link'])