# librería para leer argumentos del programa
import sys
# librería para esperar un segundo
import time

def main():
    argumentos = sys.argv
    # obtener la cantidad de segundos desde los argumentos
    segundos = argumentos[1]
    time.sleep(1)
    print(segundos)

def sigma():
    # sumamos los numeros del 1 al 100
    pass

main()