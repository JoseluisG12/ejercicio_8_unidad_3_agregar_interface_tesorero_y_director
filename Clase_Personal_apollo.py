from Clase_Personal import Personal
class deApoyo(Personal):
    __categoria : int

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad,categoria=0, areaInvest='', tipoInvest='',carrera='', cargo='', catedra='' ) -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad,categoria, areaInvest, tipoInvest, carrera,cargo, catedra)
        self.__categoria = int(categoria)

    def getcategoria(self):
        return self.__categoria

    def getsueldo(self):
        sueldo = super().getsueldoB() + (super().getantiguedad()/100)
        if self.__categoria in [1,2,3,4,5,6,7,8,9,10]:
            sueldo += (10/100)
        elif self.__categoria == [11,12,13,14,15,16,17,18,19,20]:
            sueldo += (20 / 100)
        elif self.__categoria == [21,22]:
            sueldo += (50 / 100)
        return sueldo

    def mostrardatos(self):
        super().mostrardatos()
        print("""
Datos personal de apollo:""")
        print(f"""
Categoria:{self.__categoria}""")
