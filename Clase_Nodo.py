from Clase_Personal import  Personal
class Nodo:
    __Personal : Personal
    __siguiente : object

    def __init__(self,Personal)-> None:
        self.__Personal = Personal
        self.__siguiente = None

    def setsiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getsiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__Personal

    def setDato(self,dato):
        self.__Personal = dato