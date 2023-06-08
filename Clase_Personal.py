
class Personal(object):
    __cuil : int
    __apellido : str
    __nombre : str
    __sueldoBasico : float
    __antiguedad : int

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera='', cargo='', catedra='',areaInvest='', tipoInvest='', categoria='') -> None:
        self.__cuil = int(cuil)
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = float(sueldoBasico)
        self.__antiguedad = int(antiguedad)

    def getapellido(self):
        return self.__apellido

    def setsueldo(self,sueldo):
        self.__sueldoBasico = sueldo

    def getsueldoBasico(self):
        return self.__sueldoBasico


    def mostrardatos(self):
        print("""
Datos personal:""")
        print(f"""
Cuil:{self.__cuil}
Apellido:{self.__apellido}
Nombre:{self.__nombre}
Sueldo:${self.__sueldoBasico}
Antiguedad:{self.__antiguedad}años""")

    def getnombre(self):
        return self.__nombre

    def getcuil(self):
        return self.__cuil

    def getsueldoB(self):
        return self.__sueldoBasico

    def getantiguedad(self):
        return self.__antiguedad


