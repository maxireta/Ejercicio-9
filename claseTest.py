import unittest
from claseNuevo import nuevo
from claseUsado import usado
from claseColeccion import coleccion

class testVehiculos(unittest.TestCase):
    def setUp(self):
        self.__veh = coleccion()
        self.__veh.cargar()
    def test1_2(self):
        veh = nuevo('Falcon', int(5), 'Verde', float(20000), 'Full')
        veh2 = usado('Renault', 'Kwid', int(4), 'Blanco', float(30000), 'ABC-123', int(2020), int(80000))
        self.__veh.agregarElemento(veh2)
        self.__veh.insertarElemento(veh, 0)
        vehiculos_finales = self.__veh.obtenerVehiculos()
        vehiculos_esperados = [veh, veh2]
        self.assertEqual(vehiculos_finales, vehiculos_esperados)
    def test3(self):
        pos = 2
        objeto_esperado = nuevo
        objeto_obtenido = self.__veh.obtenerElemento(pos)
        self.assertEqual(objeto_obtenido, objeto_esperado)
    def test4(self):
        pate = 'ABC123'
        self.__veh.tes4(pate)
        patente = "ABC-123"
        nuevo_precio_venta = 30000
        self.__veh.verificarPrecioVenta(patente, nuevo_precio_venta)