''' Transforma de °Celsius a Fahrenheit y Kelvin '''
# 1. Pedimos al usuario la tempratura en Celsius
celsius = input('Ingrese la tempratura en °C: ')
# 2. La transformamos a FLOAT (número con decimales)
celsius = float(celsius)
# 3. calculo la temperatura en Fahrenheit
fahr = 32 + (1.8 * celsius)
# 4. calculo grados kelvin
kelvin = celsius + 273.1
# 5. volvemos a transformar todo a string
celsius = str(celsius)
fahr = str(fahr)
kelvin = str(kelvin)
# 6. Creamos el mensaje
mensaje = 'Los ' + celsius + '°C son equivalentes a ' + fahr + '°F y a ' + kelvin + '°K'
# 7. Imprimimos el mensaje en consola
print(mensaje)

novela = '''En un lugar de la mancha
de cuyo nombre no quiero acordarme
no hace muchi tiempo ....'''
print(novela)

etiqueta = '<a href="#">Región de O\'higgins</a>'

proposicion = not ((10 > 2 + 2) and (5 < 3 or 6 > 1))
#                     True           False    True
#                     True               True
#                               True
#                               False

aprobado = 4.0 == 7.0 - 3 # True
