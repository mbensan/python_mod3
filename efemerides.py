# definimos el diccionario
efemerides = {
    '1 de enero': 'Año Nuevo',
    '27 de febrero': 'Terremoto en Chile',
    '8 de marzo': 'Día de la Mujer',
    '21 de mayo': 'Glorias Navales',
    '18 de septiembre': 'Fiestas Patrias',
    '19 de septiembre': 'Glorias del Ejercito',
    '25 de diciembre': 'Navidad'
}

# 18/9

# BONUS
def transformar_fecha(f_original):
    meses = {
        '1': 'enero', '2': 'febrero', '3': 'marzo', '4': 'abril',
        '5': 'mayo', '6': 'juni', '7': 'julio', '8': 'agosto',
        '9': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'
    }
    if '/' in f_original:
        f_array = f_original.split('/')
        f_nueva = f_array[0] + ' de ' + meses[f_array[1]]
        return f_nueva
    if '-' in f_original:
        f_array = f_original.split('-')
        f_nueva = f_array[0] + ' de ' + meses[f_array[1]]
        return f_nueva
    if '.' in f_original:
        f_array = f_original.split('.')
        f_nueva = f_array[0] + ' de ' + meses[f_array[1]]
        return f_nueva

    signo_raro = first([signo in f_original for signo in ['.', '/', '-']], None)  
    return f_original


transformar_fecha('14/3')
transformar_fecha('4-5')
transformar_fecha('20.12')
