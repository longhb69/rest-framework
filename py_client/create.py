import requests

endpoint = "http://localhost:8000/api/product/"

data = {
    "title": "This field",
    "price": 32.99
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())