from claseColeccion import coleccion
from claseTest import testVehiculos
import unittest

if __name__ == '__main__':
    cole = coleccion()
    cole.cargar()
    print("Menú:")
    print("1. Insertar un vehículo.")
    print("2. Agregar un vehículo.")
    print("3. Mostrar tipo elemento.")
    print("4. Modificar precio por patente.")
    print("5. Mostrar todos los datos.")
    print("6. Mostrar vehículos a la venta.")
    print("7. Almacenar datos.")
    print("8. Test.")
    opcion = input("Elija una opción: ")
    if opcion == '1':
        pos = int(input("Ingrese la posición: "))
        pos -= 1
        auto = cole.crearvehiculo()
        cole.insertarElemento(auto, pos)
    elif opcion == '2':
        auto = cole.crearvehiculo()
        cole.agregarElemento(auto)
    elif opcion == '3':
        posicion = int(input("Ingrese una posición: "))
        posicion -= 1
        cole.mostrar3(posicion)
    elif opcion == '4':
        pate = input("Ingrese la patente: ")
        cole.opcion4(pate)
    elif opcion == '5':
        cole.opcion5()
    elif opcion == '6':
        cole.opcion6()
    elif opcion == '7':
        cole.opcion7()
    elif opcion == '8':
        unittest.main()