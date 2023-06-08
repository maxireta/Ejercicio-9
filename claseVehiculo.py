class vehiculo:
    def __init__(self, modelo, puertas, color, precio_base):
        self.__mod = modelo
        self.__puertas = puertas
        self.__color = color
        self.__prebase = precio_base
    def getModelo(self):
        return self.__mod
    def getPuertas(self):
        return self.__puertas
    def getColor(self):
        return self.__color
    def getPrecioBase(self):
        return self.__prebase
    def setPrecio(self, nuevop):
        self.__prebase = nuevop
        #De cada vehículo desea registrar el modelo 
        # (ej. Palio, Focus, etc.), cantidad de puertas, color y el precio base de venta.