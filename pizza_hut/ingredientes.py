
def drop_ingrediente(pizza):
  string_pregunta = [str(idx) + '. ' + ingr for idx, ingr in enumerate(pizza['ingredientes'])]
  string_pregunta = '\n'.join(string_pregunta)
  string_pregunta += '\n\n'
  print('Elija un ingrediente para eliminar:')
  eleccion = int(input(string_pregunta))
  # chequeamos que el numero ingresado no sea menor a 0 y mayor o igual al largo
  if eleccion < 0 or eleccion >= len(pizza['ingredientes']):
    print('Ese ingrediente no está en la pizza')
    return

  ingrediente_electo = pizza['ingredientes'][eleccion]
  # ahora sacamos el ingrediente de la lista
  pizza['ingredientes'] = [item for item in pizza['ingredientes'] if item != ingrediente_electo]


def add_ingrediente(pizza):
  disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo', 'Jamón','Carne','Tocino','Queso']

  eleccion = input('''
    Elija un ingrediente:
    1. Tomate
    2. Champiñones
    3. Aceituna
    4. Cebolla
    5. Pollo
    6. Jamón
    7. Carne
    8. Tocino
    9. Queso
  ''')
  eleccion = int(eleccion)
  # chequeamos que el usuario elija un ingrediente exitente
  if eleccion < 1 or eleccion > 9:
    print('Ingrediente no disponible')
    return
  ingrediente_electo = disponibles[eleccion - 1]
  # chequeamos que la pizza aun no tenga ese ingrediente
  if ingrediente_electo in pizza['ingredientes']:
    print('Ese ingrediente ya está en su pizza')
    return
  pizza['ingredientes'].append(ingrediente_electo)


