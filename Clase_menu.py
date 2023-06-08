from Manejador_Personal import ITesorero
from Manejador_Personal import  Coleccion_Personal

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {1:self.op1,
                           66:self.op66,
                           2:self.op2,
                           3:self.op3,
                           4:self.op4,
                           5:self.op5,
                           6:self.op6,
                           7:self.op7,
                           9:self.op9,

                           }


    def run(self,Mpersonal,encoder):
        band = True
        while band:
            b = int(input("""
            
Menu principal:
1-insertar un agente a la coleccion
2-agregar un agente a la coleccion 
3-mostrar el tipo de objeto almacenado en una posicion
4-listar en orden alfabetico los docentes investigadores de una carrera
5-contar la cantidad de docentes investigadores e investigadores hay en un area especifica
6-mostrar nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.
9-ingresar usuario y contraseña para acceder a los metodos restringuidos
\n"""))

            func = self.__switcher.get(b)
            if func:
                func(Mpersonal,encoder)
            else:
                print("Saliendo...")
                band = False


    def op1(self,Mpersonal,encoder):
        posicion = int(input("ingrese la posicion a insertar el agente\n"))
        Mpersonal.insertarElemento(posicion)

    def op2(self,Mpersonal,encoder):
        print("agregar personal")
        Personal = Mpersonal.registrarpersonal()
        Mpersonal.agregarElemento(Personal)

    def op3(self,Mpersonal,encoder):
        posicion = int(input("ingrese la posicion del obejeto a mostrar\n")) + 1
        Mpersonal.mostrarElemento(posicion)

    def op4(self,Mpersonal,encoder):
        carrera = input("ingrese el nombre de la carrera\n")
        Mpersonal.ordenar_nombre(carrera)

    def op5(self, Mpersonal, encoder):
        area = input("ingrese un area de investigacion\n")
        contador = Mpersonal.buscararea(area)
        print(f"""
area {area}
cantidad de docente e investigadores:{contador[0]}
cantidad de investigadores:{contador[1]}""")

    def op6(self, Mpersonal, encoder):
        Mpersonal.ordenar_apellido()

    def op7(self, Mpersonal, encoder):
        categoria = int(input("ingrese la categoria a buscar\n"))
        acumulador = Mpersonal.listarcategoria(categoria)
        print(f"cantidad de dinero a solicitar para el pago de importe extra en la categoria {categoria} es :${acumulador}")

    def op9(self, Mpersonal, encoder):
        usuario = input("ingrese el usario`\n")
        contraseña = input("ingrese contraseña\n")
        if usuario == 'uTesorero':
            if contraseña == 'ag@74ck':
                print("mostrar sueldo de agene por cuil")
                Mpersonal.accesofuncionestesorero()

            else:
                print("Error contraseña incorrecta\n")

        if usuario == 'uDirector':
            if contraseña == 'ufC77#!1':
                Mpersonal.accesofuncionesdirector()
            else:
                print("Error contraseña incorrecta\n")
        if usuario != 'uDirector' and usuario != 'uTesorero':
            print("Error usuario no encontrado")



    def op66(self,Mpersonal,encoder):
        for dato in Mpersonal:
            dato.mostrardatos()


