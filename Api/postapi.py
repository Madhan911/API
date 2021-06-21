import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

file = open("C://Users//Hp//Desktop//rfiles//chinni.json", 'r')

request = file.read()

json_format = json.loads(request)

response = requests.post(url, json_format)

print(response.content)



 