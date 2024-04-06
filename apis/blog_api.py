import requests
import json
import pdb

def probar_get():
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
    text_respuesta = response.text
    print(response.text)

def probar_put():
    url = 'https://jsonplaceholder.typicode.com/POSTS/20'
    data = {
        'userId': 2,
        'title': 'Articulo Modificador',
        'body': 'Este es la corrección de mi primer posteo desde Python'
    }
    data = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.put(url, data)

    texto_respuesta = response.text
    print(texto_respuesta)
    print(response.status_code)


if __name__ == '__main__':
    probar_put()
