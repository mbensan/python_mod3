import sys

def visitar_ciudades():
    ciudades = ["Pto. Montt", 'Talca', 'Stgo', 'Valdivia', 'Viña de Mar', 'Villa Alemana', 'Antofagasta']
    #              0            1       2         3          4

    for indice, ciudad in enumerate(ciudades):
        frase = f'La ciudad {ciudad} está en la posición {indice}'
        if indice % 2 == 0:
            print(frase)

def buscar():
    buscada = sys.argv[1]
    palabras = ['En', 'un', 'lugar', 'de', 'la', 'Mancha,', 'de', 'cuyo', 'nombre', 'no', 'quiero', 'acordarme,', 'no', 'ha', 'mucho', 'tiempo', 'que', 'vivía', 'un', 'hidalgo', 'de', 'los', 'de', 'lanza', 'en', 'astillero,', 'adarga', 'antigua,', 'rocín', 'flaco', 'y', 'galgo', 'corredor.']

    la_encontramos = False
    
    for pos, palabra in enumerate(palabras):
        if palabra == buscada:
            frase = f'La palabra {buscada} está en la posición {pos}'
            print(frase)
            la_encontramos = True
            break

    if la_encontramos == False:
        print(f'La palabra {buscada} no está en el Quijote de la Mancha')


def quina ():
    '''
    lista = []
    for i in range(31):
        if i % 5 == 0:
            lista.append('QUINA')
        else:
            lista.append(i)
    '''
    # Comprehension List's
    lista = ['Quina' if i % 5 == 0 else i for i in range(1, 31, 2)]
    print(lista)

def crear_enlaces ():
    nombres = ['Home', 'Nosotros', 'Contacto']
    enlaces = ['<a href="#">' + nombre + '</a>' for nombre in nombres]
    print(enlaces)


def mostrar_semana ():
    # "semana" es una variable del tipo diccionario
    semana = {
        'lunes': 2,
        'martes': 2,
        'miercoles': 4,
        'jueves': 4,
        'viernes': 2
    }
    print(semana['miercoles'])
    for llave, valor in semana.items():
        if valor == 2:
            print(f'el dia {llave} fué un día CORTO')
        else:
            print(f'el dia {llave} fue un día LARGO')

mostrar_semana()


destinos = [
    {
        'nombre': 'Argentina',
        'prefijo': 54,
        'ciudades': ['BS AS', 'Cordova', 'Mendoza', 'Junin', 'Rio Gallegos']
    },
    {
        'nombre': 'Suecia',
        'prefijo': 47,
        'ciudades': ['Estocolmo', 'Gotemburgo', 'Malmö', 'Kiruna']
    }
]
print(destinos[1]['ciudades'][2])









