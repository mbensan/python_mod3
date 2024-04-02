'''
    Este programa nunca pierde
'''
# 1. Le pido al usuario que ingrese un número
num_usuario = input('Ingrese un número: ')
# 2. Transformar el string ingresado a número
num_usuario = int(num_usuario)
# 3. Le sumo 1 al numero del usuario
num_comp = num_usuario + 1
# 4. transformo el número de la computadora a string
num_comp = str(num_comp)
# 5. Creo la variable mensaje
mensaje = 'Yo gané con el número ' + num_comp
# 6. Le aviso al usuario el mensaje
print(mensaje)

''' 
Versión untra corta
print('Gano con el ' + str(int(input('Ingrese un numero: ')) + 1))
'''