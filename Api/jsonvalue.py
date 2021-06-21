import requests
import json
import jsonpath

url = "https://reqres.in/api/unknown"

response = requests.get(url)

json_path = json.loads(response.text)

pages = jsonpath.jsonpath(json_path, 'per_page')
print(pages[0])
