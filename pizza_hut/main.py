from ingredientes import add_ingrediente, drop_ingrediente

pizza = {
  "masa": "Masa Tradicional",
  "salsa": "Salsa de Tomate",
  "ingredientes": []
}

def menu ():
  print('Bienvenido/as a Hot Pizza')
  while True:
    opcion = input('''¿Qué desea realizar?
      1. Cambiar tipo de Masa
      2. Cambiar tipo de Salsa
      3. Agregar Ingredientes
      4. Eliminar Ingredientes
      5. Ordenar con los Ingredientes Actuales
      0. Consultar ingredientes de la pizza
      Otro Número cancelará el pedido.
      > ''')
    if opcion == '1':
      print('Cambiando masa')
    elif opcion == '2':
      print('cambiar la salsa')
    elif opcion == '3':
      add_ingrediente(pizza)
    elif opcion == '4':
      drop_ingrediente(pizza)
    elif opcion == '5':
      print('terminar la orden')
    elif opcion == '0':
      print(pizza)
    else:
      print('Opción inválida')
      break
    

if __name__ == '__main__':
  menu()