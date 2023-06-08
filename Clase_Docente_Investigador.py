from Clase_Docente import Docente
from Clase_Inversitagor import  Investigador

class Docente_Invertigador(Docente,Investigador):
    __categoria_inv : int
    __importe : float

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad,carrera='', cargo='', catedra='', areaInvest='', tipoInvest='',categoria_inv='',importe=0) -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad,carrera,cargo, catedra, areaInvest,tipoInvest)
        self.__categoria_inv = int(categoria_inv)
        self.__importe = importe






    def getimporte(self):
        return self.__importe

    def getsueldo(self):
        sueldo = super().getsueldoB()
        return sueldo

    def getcategoria(self):
        return self.__categoria_inv

    def setimporte(self,importe):
        self.__importe = importe

    def porcentaje(self,porcentaje):
        sueldo = super().__sueldoBasico



    def mostrardatos(self):
        super().mostrardatos()
        print("""
Datos docente y ayudante:""")
        print(f"""
Categoria:{self.__categoria_inv}
Importe:${self.__importe}""")