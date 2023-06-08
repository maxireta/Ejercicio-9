from claseNuevo import nuevo
from claseUsado import usado
from claseNodo import Nodo
from claseInterfaz import interfaz
import json

class coleccion(interfaz):
    __com: Nodo
    def __init__(self):
        self.__com = None
    def cargar(self):
        with open('vehiculos.json', encoding="UTF-8") as archi:
            datos = json.load(archi)
            vnuevo = datos['nuevos']
            vusado = datos['usados']
            for vehi in vnuevo:
                marca = vehi['marca']
                modelo = vehi['modelo']
                puerta = int(vehi['cantidad_puertas'])
                color = vehi['color']
                precio = float(vehi['precio_base'])
                version = vehi['version']
                veh = nuevo(modelo, puerta, color, precio, version)
                veh.setMarca(marca)
                self.agregarElemento(veh)
            for vehiculo in vusado:
                marca = vehiculo['marca']
                modelo = vehiculo['modelo']
                cantidad_puertas = int(vehiculo['cantidad_puertas'])
                color = vehiculo['color']
                precio_base = float(vehiculo['precio_base'])
                patente = vehiculo['patente']
                anio = int(vehiculo['anio'])
                kilometraje = int(vehiculo['kilometraje'])
                veh = usado(marca, modelo, cantidad_puertas, color, precio_base, patente, anio, kilometraje)
                self.agregarElemento(veh)
    def crearvehiculo(self):
        print("1. Nuevo")
        print("2. Usado.")
        opcion = input("Elija una opción: ")
        if opcion == '1':
            modelo = 'Falcon'
            puerta = int(5)
            color = 'Verde'
            precio = float(20000)
            version = 'Full'
            veh = nuevo(modelo, puerta, color, precio, version)
        else:
            marca = 'Renault'
            modelo = 'Kwid'
            cantidad_puertas = int(4)
            color = 'Blanco'
            precio_base = float(30000)
            patente = 'ABC-123'
            anio = int(2020)
            kilometraje = int(80000)
            veh = usado(marca, modelo, cantidad_puertas, color, precio_base, patente, anio, kilometraje)
        return veh

    def agregarElemento(self, veh):
        nodo = Nodo(veh)
        if self.__com == None:
            self.__com = nodo
        else:
            actual = self.__com
            while actual.getSig() is not None:
                actual = actual.getSig()
            actual.setSig(nodo)
    def insertarElemento(self, elem, pos):
        if pos < 0:
            raise IndexError("Posición inválida.")
        else:
            nodo = Nodo(elem)
            if pos == 0:
                nodo.setSig(self.__com)
                self.__com = elem
            else:
                ant = self.__com
                ins = ant.getSig()
                i = 1
                while i < pos and ins is not None:
                    ant = ins
                    ins = ant.getSig()
                ant.setSig(nodo)
                nodo.setSig(ins)
    def mostrar3(self, pos):
        if pos < 0:
            raise IndexError("Posición inválida.")
        else:
            actual = self.__com
            i = 1
            while i < pos and actual is not None:
                actual = actual.getSig()
            if isinstance(actual.getVeh(), nuevo):
                print(f"El elemento de la posición {pos + 1} es nuevo.")
            else:
                print(f"El elemento de la posición {pos + 1} es usado.")
    def opcion4(self, pate):
        actual = self.__com
        mos = actual.getVeh()
        i = 1
        while actual is not None and mos.getPatente() != pate:
            mos = actual.getVeh()
            if isinstance(actual, nuevo):
                actual = actual.getSig()
                mos = actual.getVeh()
            actual = actual.getSig()
        if actual is None:
            print("Patente no encontrada.")
        else:
            cam = self.cambiarPrecio(mos)
            actual.setVeh(cam)

    def cambiarPrecio(self, auto):
        precion = float(input("Ingrese un nuevo precio: "))
        auto.setPrecio(precion)
        self.mostrarprecio(auto)
        return auto
    def mostrarprecio(self, auto):
        print(f"Importe de venta {auto.importeVenta()}")
    def opcion5(self):
        i = 0
        actual = self.__com
        while actual != None:
            mos = actual.getVeh()
            mos.mostrarElemento(i)
            i += 1
            actual = actual.getSig()
    def opcion6(self):
        actual = self.__com
        while actual != None:
            mos = actual.getVeh()
            mos.mostrar2()
            actual = actual.getSig()
    def hacerlista(self):
        datos = []
        actual = self.__com
        while actual is not None:
            mos = actual.getVeh()
            datos.append(mos.dic())
            actual = actual.getSig()
        return datos
    def opcion7(self):
        datos = self.hacerlista()
        with open('vehiculos2.json', "w") as archi:
            json.dump(datos, archi, indent=4)
        print("Datos guardados exitosamente.")
    def obtenerVehiculos(self):
        vehiculos = []
        actual = self.__com
        while actual is not None:
            auto = actual.getVeh()
            vehiculos.append(auto)
            actual = actual.getSig()
        return vehiculos
    def obtenerElemento(self, pos):
        if pos < 0:
            raise IndexError("Posición inválida.")
        actual = self.__com
        i = 1
        while actual is not None and i < pos:
            actual = actual.getSig()
            i += 1
        if actual is None:
            retornar = None
        else:
            retornar = actual.getVeh()
        return retornar
    def tes4(self, pate):
        actual = self.__com
        mos = actual.getVeh()
        i = 1
        while actual is not None and mos.getPatente() != pate:
            mos = actual.getVeh()
            if isinstance(actual, nuevo):
                actual = actual.getSig()
                mos = actual.getVeh()
            actual = actual.getSig()
        if actual is None:
            print("Patente no encontrada.")
        else:
            cam = self.tes42(mos)
            actual.setVeh(cam)
    def cambiarPrecio(self, auto):
        precion = float(30000)
        auto.setPrecio(precion)
        return auto
    def verificarPrecioVenta(self, patente, nuevo_precio_venta):
        actual = self.__com
        while actual is not None:
            vehiculo = actual.getVeh()
            if isinstance(vehiculo, usado) and vehiculo.getPatente() == patente:
                vehiculo.setPrecioVenta(nuevo_precio_venta)
                precio_venta_actual = vehiculo.getPrecioVenta()
                if precio_venta_actual == nuevo_precio_venta:
                    print(f"El precio de venta del vehículo con patente {patente} ha sido verificado correctamente.")
                else:
                    print(f"Error en la verificación del precio de venta del vehículo con patente {patente}.")
                return
            actual = actual.getSig()
        print("No se encontró ningún vehículo usado con la patente especificada.")