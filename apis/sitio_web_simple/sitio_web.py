import requests
import json

# 1. Solicito las imagenes
url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)

# 2. Transormo el resultado a una lista de cosas
photos = json.loads(response.text)

# 3. Acortamos la lista a las primeras 8
photos = photos[0:8]

# 4. Armamos el texto que contiene todas las col's 3
cols_3 = ''
for photo in photos:
    cols_3 += f'''
        <div class="col-3">
            <div class="card">
            <img class="w-100" src="{photo['url']}" alt="">
            <h4>{photo['title']}</h4>
            </div>
        </div>
    '''

# 5. Armamos el HTML completo
html_completo = f'''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Bootstrap demo</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>
    <body>
        <h1 class="text-center">Blog Simple</h1>
        <div class="container">
        <div class="row">
            <!-- Acá van las col-3's -->
            {cols_3}
        </div>
        </div>
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
    </html>
'''

print(html_completo)
# 6. Crear un archivo HTML y agregar el texto completo


