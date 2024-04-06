import requests
import json
from html_maker import make_col3s, make_full_html

# 1. Solicito las imagenes
url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)

# 2. Transormo el resultado a una lista de cosas
photos = json.loads(response.text)

# 3. Acortamos la lista a las primeras 8
photos = photos[0:8]

# 4. Armamos el texto que contiene todas las col's 3
cols_3 = make_col3s(photos)

# 5. Armamos el HTML completo
html_completo = make_full_html(cols_3)

# 6. Crear un archivo HTML y agregar el texto completo
archivo = open('output.html', 'w', encoding='utf-8')
archivo.write(html_completo)
archivo.close()
