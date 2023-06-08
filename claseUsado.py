from claseVehiculo import vehiculo
from claseInterfaz import interfaz
import datetime

class usado(vehiculo, interfaz):
    def __init__(self, marca, modelo, puertas, color, precio_base, patente, anio, kilometraje):
        super().__init__(modelo, puertas, color, precio_base)
        self.__marca = marca
        self.__patente = patente
        self.__anio = anio
        self.__kilo = kilometraje
    def getPatente(self):
        return self.__patente
    def setPrecio(self, nuevop):
        super().setPrecio(nuevop)
    def importeVenta(self):
        actual = datetime.datetime.now().year
        base = super().getPrecioBase()
        antiguedad = 0.01 * (actual - self.__anio) * base
        if self.__kilo > 100000:
            kilom = 0.02 * base
        else:
            kilom = 0
        importe = base - antiguedad - kilom
        return importe
    def mostrarElemento(self, pos):
        pos += 1
        print(f"Elemento usado: {pos}")
        print(f"Marca: {self.__marca}, Modelo: {super().getModelo()}, Puertas: {super().getPuertas()}")
        print(f"Color: {super().getColor()}, Precio Base: {super().getPrecioBase()}, Patente: {self.__patente}")
        print(f"Año: {self.__anio}, Kilometraje: {self.__kilo}, Importe: {self.importeVenta()}")
    def mostrar2(self):
        print(f"Modelo: {super().getModelo()}, Puertas: {super().getPuertas()}, Importe: {self.importeVenta()}")
    def dic(self):
        return {
            "marca": self.__marca,
            "modelo": super().getModelo(),
            "cantidad_puertas": super().getPuertas(),
            "color": super().getColor(),
            "precio_base": super().getPrecioBase(),
            "patente": self.__patente,
            "anio": self.__anio,
            "kilometraje": self.__kilo
        }