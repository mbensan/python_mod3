import getpass

def validarPassword(password):
    # 1. validamos que sea de largo al menos 6
    if len(password) < 6:
        print('Su contraseña debe contener al menos 6 caracteres')
        return False
    elif password == '12345678':
        print('Ese password es muy sencillo. Elija otro')
        return False
    elif password == '87654321':
        print('Ese password es muy sencillo. Elija otro')
        return False
    elif ("'" in password) or ('"' in password):
        print("No puede usar el caracter ' dentro de su password")
        return False
    else:
        print('Contraseña correcta')
        return True

def main():
    while True:
        # 1. Le pido la nueva contraseña al usuario
        password = getpass.getpass('Ingrese una contraseña: ')
        # 2. Valido la contraseña usando la funcion "validarPassword"
        esCorrecta = validarPassword(password)
        if esCorrecta:
            break

    print("Bienvenido al sistema")

main()
