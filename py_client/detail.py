import requests

endpoint = "http://localhost:8000/api/product/1/"
get_response = requests.get(endpoint, json={"title": "abc","content": "Hello World"})
print(get_response.json())