import sys

def word_count():
    # 1. obtenemos el nombre del archivo
    nombre_archivo = sys.argv[1]
    # 2. leemos el contenido del archivo
    with open(nombre_archivo, "r") as file:
        texto = file.read()
    # 3. Contamos las letras 
    texto_sin_espacios = [letra for letra in texto if letra != ' ']
    print(f'En el archivo hay (sin contar los espacios) {len(texto_sin_espacios)} letras')
    # 4. Contamos las palabras
    num_palabras = len(texto.split(' '))
    print(f'Hay {num_palabras} palabras')


word_count()

eventos [
    ['2022-09-18', '20:00', 'Bailar Cueca'],
    ['2022-01-03', '21:00', 'Se te aparecio marzo'],
    ['2022-01-01', '07:00', 'Salir a correr']
]
eventos.sort(CRITERIO)

