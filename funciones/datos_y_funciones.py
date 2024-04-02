import sys

precios = {
  'Notebook': 700000,
  'Teclado': 25000,
  'Mouse': 12000,
  'Monitor': 250000,
  'Escritorio': 135000,
  'Tarjeta de Video': 1500000
}
# python datos_funciones.py 10000 
# python datos_funciones.py 10000 menor
# python datos_funciones.py 10000 otra_cosa # MAL!
def filtro():
  operacion = None
  umbral = int(sys.argv[1])

  if len(sys.argv) < 3:
    operacion = 'mayor'
  elif sys.argv[2] == 'menor':
    operacion = 'menor'
  else:
    print('Operación no válida')
    sys.exit()
  # acá guardamos los elementos que SI pasaron el filtro
  filtrados = []
  for producto, precio in precios.items():
    if operacion == 'mayor' and precio > umbral:
      filtrados.append(producto)
    elif operacion == 'menor' and precio < umbral:
      filtrados.append(producto)
  
  filtrados = ', '.join(filtrados)
  print(f'Los elementos que son {operacion} a {umbral} son {filtrados}')

# filtro()

''' TODO: Hacer esta función recursiva'''
def factorial(num):
  '''
    1! = 1
    5! = 5 * 4 * 3 * 2 * 1
    10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
  '''
  # caso base
  if num <= 1:
    return 1
  # caso genérico
  return num * factorial(n - 1)



def productoria(lista):
  total = 1
  for elem in lista:
    total = total * elem
  return total

# print(factorial(10))
def calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6):
  print(f'el factorial de {fact_1} es {factorial(fact_1)}')
  print(f'la productoria de {prod_1} es {productoria(prod_1)}')
  print(f'el factorial de {fact_2} es {factorial(fact_2)}')

calcular(10, [3, 0, 123])
