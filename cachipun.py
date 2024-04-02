import random
''' Vamos a jugar cachipun con el usuario'''
# 1. Vamos a pedir la jugada del usuario
jugada_usuario = input('Ingrese su jugada:\n1: Piedra\n2:Papel\n3: Tijeras\n')

# 2. General la jugada del computador
jugada_cpu = random.randint(1, 3)

# 3. Transformo la jugada del computador a string
jugada_cpu = str(jugada_cpu)

print('jugada del computador ' + jugada_cpu)

# 4. Resolvemos quien gana
if jugada_usuario == '1': # usuario eligió piedra
    if jugada_cpu == '1':
        print('EMPATE: Ambos eligieron PIEDRA')
    elif jugada_cpu == '2':
        print('GANA CPU: PAPEL contra PIEDRA')
    else: # jugada_cpu == '3'
        print('GANA Usted: PIEDRA contra TIJERAS')
elif jugada_usuario == '2': # usuario eligió papel
    pass
elif jugada_usuario == '3': # usuario elig+gió tijeras
    pass
else:
    print('Opción no válida')
