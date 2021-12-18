import requests
import json

datos={
  "email": "escuela.joshua@gmail.com",
  "assistantId": "16bf2dfd-606a-4065-a7a6-4161b12a4c26",
  "url": "https://api.us-east.assistant.watson.cloud.ibm.com/instances/76565e82-1a02-47fb-a07f-4cf2e3b0dc0c",
  "skillId": "1ea4fc9e-affd-4f8b-adfb-8c1d2972d6c5",
  "apiKey": "9xMWrRUB3uOD4H6PTXIujgDtjvuwvVil8N9gFubsmHFH",
  "submitConfirmation": False
}

response = requests.post('http://172.21.188.211:3000/submit', json=json.dumps(datos)).text()
print(response)
