class Nodo:
    __veh: object
    __sig: object
    def __init__(self, auto):
        self.__veh = auto
        self.__sig = None
    def setSig(self, sig):
        self.__sig = sig
    def setVeh(self, veh):
        self.__veh = veh
    def getSig(self):
        return self.__sig
    def getVeh(self):
        return self.__veh
