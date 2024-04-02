import sys
from string import ascii_lowercase

def fuerza_bruta ():
    clave = sys.argv[1].lower()
    intentos = 0
    for letra in clave:
        for caracter in ascii_lowercase:
            intentos += 1
            if letra == caracter:
                break
    print(f'Se logro romper la contraseña en {intentos} intentos')


def mostrar_argumentos():
    for indice, palabra in enumerate(sys.argv):
        print(f'En la posición {indice} de los argumentos viene: {palabra}')

#fuerza_bruta()
mostrar_argumentos()