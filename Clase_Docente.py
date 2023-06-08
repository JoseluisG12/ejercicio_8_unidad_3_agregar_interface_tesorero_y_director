from Clase_Personal import Personal
class Docente(Personal):
    __carrera : str
    __cargo : str
    __catedra : str

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad,carrera='', cargo='', catedra='', areaInvest='', tipoInvest='', categoria='') -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, areaInvest, tipoInvest, categoria)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def getcargo(self):
        return self.__cargo

    def getcarrera(self):
        return self.__carrera

    def getsueldo(self,porcentaje):
        sueldo = super().getsueldoB() + (super().getantiguedad()/100)
        if self.__cargo == 'simple':
            sueldo += (10/100)
        elif self.__cargo == 'semiexclusivo':
            sueldo += (20 / 100)
        elif self.__cargo == 'exclusivo':
            sueldo += (50 / 100)
        return sueldo

    def mostrardatos(self):
        super().mostrardatos()
        print("""
Datos docente:""")
        print(f"""
Carrera:{self.__carrera}
Cargo:{self.__cargo}
catedra:{self.__catedra}""")
