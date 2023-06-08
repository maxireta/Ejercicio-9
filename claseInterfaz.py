from abc import ABC, abstractmethod

class interfaz:
    @abstractmethod
    def insertarElemento(self, elem, pos):
        pass
    @abstractmethod
    def agregarElemento(self, elem):
        pass
    @abstractmethod
    def mostrarElemento(self, pos):
        pass