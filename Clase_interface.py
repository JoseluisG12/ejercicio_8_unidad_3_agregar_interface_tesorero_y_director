from zope.interface import Interface
from  abc import ABC, abstractmethod
class IColeccion (Interface):
    @abstractmethod
    def insertarVehiculo (self,posicion):
        pass

    @abstractmethod
    def agregarelemento (self):
        pass

    @abstractmethod
    def mostrarVehiculo (self):
        pass