from claseVehiculo import vehiculo
from claseInterfaz import interfaz

class nuevo(vehiculo, interfaz):
    __marca = ''
    def __init__(self, modelo, puertas, color, precio_base, version):
        super().__init__(modelo, puertas, color, precio_base)
        self.__version = version
    @classmethod
    def getMarca(cls):
        return cls.__marca
    @classmethod
    def setMarca(cls, marcan):
        cls.__marca = marcan 
    def importeVenta(self):
        base = super().getPrecioBase()
        patente = 0.10 * base
        if self.__version == 'full':
            fully = 0.02 * base
        else:
            fully = 0
        importe = base + patente + fully
        return importe
    def mostrarElemento(self, pos):
        pos += 1
        print(f"Elemento nuevo: {pos}")
        print(f"Marca: {self.getMarca()}, Modelo: {super().getModelo()}, Puertas: {super().getPuertas()}")
        print(f"Color: {super().getColor()}, Precio Base: {super().getPrecioBase()}, versión: {self.__version}, importe: {self.importeVenta()}")
    def mostrar2(self):
        print(f"Modelo: {super().getModelo()}, Puertas: {super().getPuertas()}, Importe: {self.importeVenta()}")
    def dic(self):
        return {
            "marca": self.getMarca(),
            "modelo": super().getModelo(),
            "cantidad_puertas": super().getPuertas(),
            "color": super().getColor(),
            "precio_base": super().getPrecioBase(),
            "version": self.__version
        }