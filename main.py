from os import system
import time

def selector():
    return input('Seleccione una opcion \n'
               'Presione 0 para finalizar el programa \n'
               'Presione 1 para agregar producto \n'
               'Presione 2 para eliminar un producto \n'
               'Presione 3 para actualizar la cantidad de un producto\n'
               'Presione 4 para actualizar el precio de un producto\n'
               'Presione 5 para ver el precio total de los productos\n'
               'Presione 6 para buscar algun producto\n'
               'Presione 7 para mostrar el inventario  \n')
   

def validateType(entrada, tipo, situacion):
    try:
        return tipo(entrada)
    except ValueError:
        return validateType(input(f"Se esperaba un dato de tipo {tipo.__name__}. Para {situacion} Inténtelo de nuevo: "), tipo, situacion)

def addProduct(inventario, nombre, cantidad, precio):
    system("cls")
    if len(inventario) >= 1:
        if bool(list(filter(lambda product: product[0].lower() == nombre.lower(), inventario))):
            print('\nNO SE PUEDE CREAR UN PRODUCTO QUE YA EXISTE EN EL INVENTARIO\n')
        else:
            inventario.append([nombre, validateType(cantidad, int, 'la cantidad'), validateType(precio, float, 'el precio')])
            print(f'El artículo {nombre} ha sido agregado con éxito\n')
    else:
        inventario.append([nombre, validateType(cantidad, int, 'la cantidad'), validateType(precio, float, 'el precio')])
        print(f'El artículo {nombre} ha sido agregado con éxito\n')

    time.sleep(2)
    return menu(inventario, selector())

def delProduct(inventario, nombre):
    system("cls")
    if len(inventario) == 0:
        print('\n----------NO SE PUEDE ELIMINAR PRODUCTOS DE UNA LISTA VACÍA----------\n')
    elif bool(list(filter(lambda product: product[0].lower() == nombre.lower(), inventario))):
        print('\nPRODUCTO ',nombre, ' ELIMINADO CON EXITO\n')
        time.sleep(2)
        return menu(list(filter(lambda product: product[0].lower() != nombre.lower(), inventario)), selector())
    else:
        print('\nNo se encontró el producto\n')
        
    time.sleep(2)
    return menu(inventario, selector())

def updateQuantity(inventario, producto, cantidad):
    system("cls")
    if len(inventario) == 0:
        print('\n----------NO SE PUEDE ELIMINAR PRODUCTOS DE UNA LISTA VACÍA----------\n')
    elif  bool(list(filter(lambda product: product[0].lower() == producto.lower(), inventario))):
        def update_product(product):
            if product[0].lower() == producto.lower():
                return [product[0], validateType(cantidad, int, 'la cantidad'), product[2]]
            else:
                return product
        
        print('\nEL PRODUCTO ', producto, ' HA SIDO ACTUALIZADO\n')
        time.sleep(2)
        return menu((list(map(update_product, inventario))),selector())
    else:
        print('\nEL PRODUCTO NO SE ENCONTRÓ\n')
        
    time.sleep(2)
    return menu(inventario, selector())

def updatePrice(inventario, producto, precio):
    system("cls")
    if len(inventario) == 0:
        print('\n----------NO SE PUEDE ELIMINAR PRODUCTOS DE UNA LISTA VACÍA----------\n')
    elif  bool(list(filter(lambda product: product[0].lower() == producto.lower(), inventario))):
        def update_product(product):
            if product[0].lower() == producto.lower():
                return [product[0], product[1], validateType(precio, float, 'el precio')]
            else:
                return product
        
        print('\nEL PRODUCTO ', producto, ' HA SIDO ACTUALIZADO\n')
        time.sleep(2)
        return menu(list(map(update_product, inventario)),selector())
    else:
        print('\nEL PRODUCTO NO SE ENCONTRÓ\n')
        
    time.sleep(2)
    return menu(inventario, selector())

def searchProduct(inventario,nombre):
    system("cls")
    if len(inventario) == 0:
        system("cls")
        print('\n----------NO SE PUEDE BUSCAR PRODUCTOS DE UNA LISTA VACÍA----------\n')
    elif list(filter(lambda product: product[0].lower() == nombre.lower(), inventario)):
        print('\nProducto encontrado:\n')
        print('\n'.join(map(lambda product: f"Producto: {product[0]}, Cantidad: {product[1]}, Precio: {product[2]}",list(filter(lambda product: product[0].lower() == nombre.lower(), inventario)))))
    else:
        print('No se encontró el producto')
    time.sleep(2)
    return menu(inventario, selector())

def total(inventario):
    system("cls")
    print('\nEl total de todos los productos es: ', round(sum(map(lambda product: float(product[1]) * float(product[2]), inventario)), 2))
    time.sleep(2)
    return menu(inventario, selector())
        
def showList(inventario):
    system('cls')
    if len(inventario) >= 1:
        print('----------INVENTARIO-----------\n')
        print(f"{'Producto':<15} {'Cantidad':<10} {'Precio':<10}")
        print("-" * 35)
        
        print('\n'.join(map(lambda product: f"{product[0]:<15} {product[1]:<10} {product[2]:<10.2f}", sorted(inventario))))
        print("-" * 35)
        print('')
    else:
        print('Inventario Vacío\n')

    time.sleep(2)
    return menu(inventario, selector())


def menu(inventario, opcion):
    if opcion == '0':
        system('cls')
        print('Fin del programa\n')
        time.sleep(1)
    elif opcion == '1':
        addProduct(inventario,
            input('ingrese el nombre del producto: '),
            validateType(input('ingrese la cantidad que desea ingresar: '), int, 'la cantidad'),
            validateType(input('Ingrese el precio: '), float, 'el precio'))
    elif opcion == '2':
        delProduct(inventario, input('ingrese el nombre del producto a eliminar: '))
    elif opcion == '3':
        updateQuantity(inventario,input('ingrese el nombre del producto que desea cambiar la cantidad: '),validateType(input('ingrese la cantidad que desea ingresar: '), int, 'la cantidad'))
    elif opcion == '4':
        updatePrice(inventario,input('ingrese el nombre del producto que desea cambiar el precio: '),validateType(input('Ingrese el precio: '), float, 'el precio'))
    elif opcion == '5':
        total(inventario)
    elif opcion == '6':
        searchProduct(inventario, input('Introduzca el nombre del producto a buscar: '))
    elif opcion == '7':
        showList(inventario)
    else:
        system('cls')
        print('OPCION NO VALIDA, INTRODUZCA UNA DE LAS OPCIONES PREDEFINIDAS\n')
        time.sleep(2)
        return menu(inventario, selector())
        
menu([], selector())