from Clase_Personal import Personal
class Investigador(Personal):
    __areaInvest : str
    __tipoInvest : str

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvest='', tipoInvest='', categoria='',carrera='', cargo='', catedra='') -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvest, tipoInvest, categoria, carrera,cargo, catedra)
        self.__areaInvest = areaInvest
        self.__tipoInvest = tipoInvest


    def getarea(self):
        return self.__areaInvest

    def getsueldo(self):
        sueldo = super().getsueldoB() + (super().getantiguedad()/100)
        return sueldo
    def mostrardatos(self):
        super().mostrardatos()
        print("""
Datos invertigador:""")
        print(f"""
Area:{self.__areaInvest}
Tipo:{self.__tipoInvest}""")