import requests
import json
import pdb

url = 'https://jsonplaceholder.typicode.com/POSTS'
data = {
    'userId': 1,
    'title': 'Holaps',
    'body': 'Este es mi primer posteo desde Python'
}
'''
json.loads => transformar desde JSON (texto) a un Diccionario Python
json.dumps => transformar desde un Diccionario Python a un JSON (texto)
'''
data = json.dumps(data)
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers, data)
print(response.text)
pdb.set_trace()
