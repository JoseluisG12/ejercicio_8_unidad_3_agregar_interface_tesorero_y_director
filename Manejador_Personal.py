from zope.interface import Interface
from zope.interface import implementer
from abc import ABC, abstractmethod
from Clase_Nodo import Nodo
from Clase_Docente import Docente
from Clase_Inversitagor import Investigador
from Clase_Personal_apollo import  deApoyo
from Clase_Docente_Investigador import Docente_Invertigador
import json

class ITesorero(Interface):
    @abstractmethod
    def gastosSueldoPorEmpleado(self,dni):
        pass


class IDirector(Interface):
    @abstractmethod
    def modificarBasico(self,cuil, nuevoBasico):
        pass

    @abstractmethod
    def modificarPorcentajeporcargo(self,cuil,nuevoPorcentaje):
        pass

    @abstractmethod
    def modificarPorcentajeporcategoría(self,cuil, nuevoPorcentaje):
        pass

    @abstractmethod
    def modificarImporteExtra(self,cuil, nuevoImporteExtra):
        pass
"""
la interfaz Icoleccion puede insertar un elemento el la lista en una poscicion indicada siempre y cuando este dentro de los limites de ella ta,
puede agregar un elemento al finala de la lista y mostrar un elemento segun una posicion especifica
los metodos a utilizar son insertarElemento () agregarElemento () mostrarElemento ()
"""


class IColeccion(Interface):
    @abstractmethod
    def insertarElemento(self,posicion):
        pass

    @abstractmethod
    def agregarElemento(self,Personal):
        pass

    @abstractmethod
    def mostrarElemento(self,posicion):
        pass

def Tesorero (ManejarTesorero:ITesorero):
    cuil = int(input("ingrese el cuil del agente a saber el sueldo"))
    ManejarTesorero.gastosSueldoPorEmpleado(cuil)

def Director(ManejarDirector:IDirector):
    print("acceso a diector")
    b= int(input("""
Menu Director:
1-Modificar sueldo basico segun cuil
2-modificar porcentaje que se paga por cargo
3-modificar porcentaje por categoria
4-modificar importe extra que se paga por cargo
\n"""))
    while b != 0:

        if b == 1:
            cuil = int(input("ingrese el cuil del agente a modificar el sueldo basico\n"))
            sueldo = float(input("ingrese el nuevo sueldo basico\n"))
            ManejarDirector.modificarBasico(cuil,sueldo)
        if b == 2:
            cuil = int(input("ingrese el cuil del agente a modificar el sueldo basico\n"))
            porcentaje = int(input("ingrese el nuevo valor del porcentaje del 1 al 100%"))
            ManejarDirector.modificarPorcentajeporcargo(cuil,porcentaje)
        if b == 3:
            cuil = int(input("ingrese el cuil del agente a modificar el sueldo basico\n"))
            porcentaje = int(input("ingrese el nuevo valor del porcentaje del 1 al 100%"))
            ManejarDirector.modificarPorcentajeporcategoría(cuil,porcentaje)
        if b == 4:
            cuil = int(input("ingrese el cuil del agente a modificar el sueldo basico\n"))
            importe = float(input("ingrese el importe extra nuevo por cargo de docente e investigador\n"))
            ManejarDirector.modificarImporteExtra(cuil,importe)

        b = int(input("""
        Menu Director:
        1-Modificar sueldo basico segun cuil
        2-modificar porcentaje que se paga por cargo
        3-modificar porcentaje por categoria
        4-modificar importe extra que se paga por cargo
        \n"""))


@implementer(ITesorero)
@implementer(IDirector)
@implementer(IColeccion)
class Coleccion_Personal:
    __comienzo = Nodo
    __actual = Nodo
    __indice = 0
    __tope = 0

    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getsiguiente()
            return dato

    def __iter__(self):
        return self

    def agregarElemento(self, Personal):
        nodo = Nodo(Personal)
        nodo.setsiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def cargararchivo(self,encoder):
        Personal_json = encoder.leerJSONArchivo('Personal.json')
        for Personal_json in Personal_json["Coleccion_Personal"]:
            if Personal_json["__class__"] == "Docente":
                personal = Docente(Personal_json["__atributos__"]["cuil"], Personal_json["__atributos__"]["apellido"], Personal_json["__atributos__"]["nombre"], Personal_json["__atributos__"]["sueldoBasico"], Personal_json["__atributos__"]["antiguedad"], Personal_json["__atributos__"]["carrera"], Personal_json["__atributos__"]["cargo"], Personal_json["__atributos__"]["catedra"])
                self.agregarElemento(personal)
            elif Personal_json["__class__"] == "Investigador":
                personal = Investigador(Personal_json["__atributos__"]["cuil"], Personal_json["__atributos__"]["apellido"], Personal_json["__atributos__"]["nombre"], Personal_json["__atributos__"]["sueldoBasico"], Personal_json["__atributos__"]["antiguedad"], Personal_json["__atributos__"]["areaInvest"], Personal_json["__atributos__"]["tipoInvest"])
                self.agregarElemento(personal)
            elif Personal_json["__class__"] == "deApoyo":
                personal = deApoyo(Personal_json["__atributos__"]["cuil"],Personal_json["__atributos__"]["apellido"],Personal_json["__atributos__"]["nombre"],Personal_json["__atributos__"]["sueldoBasico"],Personal_json["__atributos__"]["antiguedad"],Personal_json["__atributos__"]["categoria"])
                self.agregarElemento(personal)
            elif Personal_json["__class__"] == "Docente_Invertigador":
                personal = Docente_Invertigador(Personal_json["__atributos__"]["cuil"],Personal_json["__atributos__"]["apellido"],Personal_json["__atributos__"]["nombre"],Personal_json["__atributos__"]["sueldoBasico"],Personal_json["__atributos__"]["antiguedad"], Personal_json["__atributos__"]["carrera"], Personal_json["__atributos__"]["cargo"], Personal_json["__atributos__"]["catedra"],Personal_json["__atributos__"]["areaInvest"],Personal_json["__atributos__"]["tipoInvest"],Personal_json["__atributos__"]["cat"],Personal_json["__atributos__"]["importe"])
                self.agregarElemento(personal)

    def insertarElemento(self,posicion):
        print("___ingrese_los_datos_del_agente(docente,investigador,personal de apoyo,docente y investigador)")
        agente = input("ingrese el tipo de agente a ingresar\n")
        cuil = input("ingrese el cuil\n")
        apellido = input("ingrese el apellido\n")
        nombre = input("ingrese el nombre\n")
        sueldo = float(input("ingrese el sueldo basico`\n"))
        antiguedad = int(input("ingre la antiguedad\n"))
        if agente == 'docente':
            carrera = input("ingrese la carrera\n")
            cargo = input("ingrese el cargo\n")
            catedra = input("ingrse la catedra\n")
            unagente = Docente(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra)
        elif agente == 'investigador':
            area = input("ingrese el area de investigacion\n")
            tipo = input("ingrese el tipo de investigacion\n")
            unagente = Investigador(cuil, apellido, nombre, sueldo, antiguedad,area,tipo)
        elif agente == 'personal de apoyo':
            categoria = input("ingrese categoria\n")
            unagente = deApoyo(cuil, apellido, nombre, sueldo, antiguedad,categoria)
        elif agente =='docente y investigador':
            carrera = input("ingrese la carrera\n")
            cargo = input("ingrese el cargo\n")
            catedra = input("ingrse la catedra\n")
            area = input("ingrese el area de investigacion\n")
            tipo = input("ingrese el tipo de investigacion\n")
            categoria = input("ingrese categoria\n")
            importe = float(input("ingrese el importe\n"))
            unagente = Docente_Invertigador(cuil, apellido, nombre, sueldo, antiguedad,carrera,cargo,catedra,area,tipo,categoria,importe)
        nuevo_nodo = Nodo(unagente)
        if posicion == 1:
            nuevo_nodo.setsiguiente(self.__comienzo)
            self.__comienzo = nuevo_nodo
            self.__actual=nuevo_nodo
            self.__tope+=1
        else:
            nodo_anterior = self.__comienzo
            try:
                for i in range(posicion - 2):
                    nodo_anterior = nodo_anterior.getSiguiente()
                nuevo_nodo.setsiguiente(nodo_anterior.getSiguiente())
                nodo_anterior.setSiguiente(nuevo_nodo)
                self.__tope += 1
            except:
                print("Error la posicion se sale del rango de la lista")


    def registrarpersonal(self):
        print("___ingrese_los_datos_del_agente(docente,investigador,personal de apoyo,docente y investigador)")
        agente = input("ingrese el tipo de agente a ingresar\n")
        cuil = input("ingrese el cuil\n")
        apellido = input("ingrese el apellido\n")
        nombre = input("ingrese el nombre\n")
        sueldo = float(input("ingrese el sueldo basico`\n"))
        antiguedad = int(input("ingre la antiguedad\n"))
        if agente == 'docente':
            carrera = input("ingrese la carrera\n")
            cargo = input("ingrese el cargo\n")
            catedra = input("ingrse la catedra\n")
            unagente = Docente(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra)
        elif agente == 'investigador':
            area = input("ingrese el area de investigacion\n")
            tipo = input("ingrese el tipo de investigacion\n")
            unagente = Investigador(cuil, apellido, nombre, sueldo, antiguedad, area, tipo)
        elif agente == 'personal de apoyo':
            categoria = input("ingrese categoria\n")
            unagente = deApoyo(cuil, apellido, nombre, sueldo, antiguedad, categoria)
        elif agente == 'docente y investigador':
            carrera = input("ingrese la carrera\n")
            cargo = input("ingrese el cargo\n")
            catedra = input("ingrse la catedra\n")
            area = input("ingrese el area de investigacion\n")
            tipo = input("ingrese el tipo de investigacion\n")
            categoria = input("ingrese categoria\n")
            importe = float(input("ingrese el importe\n"))
            unagente = Docente_Invertigador(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra, area,
                                            tipo, categoria, importe)
        return unagente

    def agregarElemento(self,Personal):
        nodo = Nodo(Personal)
        nodo.setsiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def mostrarElemento(self,posicion):
        aux = self.__comienzo
        contador = self.__tope
        encontrado = False
        if posicion == contador:
            print(type(self.__actual.getDato()))
            encontrado = True
        else:

            aux = aux.getsiguiente()
            while (not encontrado and aux != None and (posicion < self.__tope and posicion > 0)):
                if posicion == contador:
                    encontrado = True
                else:
                    aux = aux.getsiguiente()
                    contador -= 1
            if encontrado:
                print(type(aux.getDato()))
                return contador
            else:
                print("no se encntro un objeto en la posicion indicada")

    def ordenar_nombre(self,carrera):
        aux = self.__comienzo

        while aux != None:

            siguiente = aux.getsiguiente()
            while siguiente is not None:

                if aux.getDato().getnombre() > siguiente.getDato().getnombre()  :
                    if isinstance(siguiente.getDato(), Docente_Invertigador):
                        if aux.getDato().getcarrera() == carrera:
                            siguiente.getDato().mostrardatos()
                else:
                    if isinstance(aux.getDato(), Docente_Invertigador) :
                        if aux.getDato().getcarrera() == carrera:
                             aux.getDato().mostrardatos()
                    aux = siguiente
                siguiente = siguiente.getsiguiente()
            aux = aux.getsiguiente()

    def buscararea(self,area):
        contador = [0]*2
        aux = self.__comienzo
        for i in range(self.__tope):
            if isinstance(aux.getDato(), Docente_Invertigador):
                if aux.getDato().getarea() == area:
                    contador[0] += 1
                    aux = aux.getsiguiente()
                else:
                    aux = aux.getsiguiente()
            elif isinstance(aux.getDato(),Investigador):
                if aux.getDato().getarea() == area:
                    contador[1] += 1
                    aux = aux.getsiguiente()
                else:
                    aux = aux.getsiguiente()
            else:
                aux = aux.getsiguiente()
        return contador

    def ordenar_apellido(self):
        if self.__comienzo is None:
            return
        # Ordenar la lista por apellido utilizando el algoritmo de ordenamiento burbuja
        ordenado = False
        while not ordenado:
            actual = self.__comienzo
            ordenado = True
            while actual.getsiguiente() is not None:
                siguiente = actual.getsiguiente()
                if actual.getDato().getapellido() > siguiente.getDato().getapellido():
                    temp = actual.getDato()
                    actual.setDato(siguiente.getDato())
                    siguiente.setDato(temp)
                    ordenado = False
                actual = actual.getsiguiente()
        # Mostrar los objetos ordenados sin repetir los apellidos
        apellidos_mostrados = set()
        actual = self.__comienzo
        while actual is not None:
            if actual.getDato().getapellido() not in apellidos_mostrados:
                print(f"""
Tipo de agente:{type(actual.getDato())}
Nombre:{actual.getDato().getnombre()}
Apellido_{actual.getDato().getapellido()}
sueldo:${actual.getDato().getsueldoBasico()}""")
                apellidos_mostrados.add(actual.getDato().getapellido())
            actual = actual.getsiguiente()

    def listarcategoria(self, categoria):
        aux = self.__comienzo
        acumulador = 0
        for i in range(self.__tope):
            if isinstance(aux.getDato(),Docente_Invertigador):
                if aux.getDato().getcategoria() == categoria:
                    print(f"""Nombre: {aux.getDato().getnombre()} Apellido: {aux.getDato().getapellido()} Importe extra: ${aux.getDato().getimporte()}""")
                    acumulador += aux.getDato().getsueldo()

            aux = aux.getsiguiente()
        return acumulador
    def accesofuncionestesorero(self):
        Tesorero(ITesorero(self))





    def gastosSueldoPorEmpleado(self,cuil):
        band = True
        i = 0
        aux = self.__comienzo
        while band and i < self.__tope:
            if aux.getDato().getcuil() == cuil:

                band = False
            else:
                i += 1
                aux = aux.getsiguiente()
        if not band:
            print(f"""
agente: {cuil}
sueldo: ${aux.getDato().getsueldo()}""")

    def accesofuncionesdirector(self):
        Director(IDirector(self))

    def modificarBasico(self,cuil,sueldo):

        band = True
        i = 0
        aux = self.__comienzo
        while band and i < self.__tope:
            if aux.getDato().getcuil() == cuil:
                band = False
            else:
                i += 1
                aux = aux.getsiguiente()

        if not band:
            aux.getDato().setsueldo(sueldo)

    def modificarPorcentajeporcargo(self,cuil, porcentaje):
        band = True
        i = 0
        aux = self.__comienzo
        while band and i < self.__tope :
            try:
                if aux.getDato().getcuil() == cuil:
                    band = False
                else:
                    i += 1
                    aux = aux.getsiguiente()
            except:
                print("cuil de agente no registrado")
                band = False

        if not band:
                sueldo = aux.getDato().getsueldoBasico() + (((aux.getDato().getantiguedad() / 100)) + (porcentaje / 100))
                round(sueldo,2)
                aux.getDato().setsueldo(sueldo)
                aux.getDato().mostrardatos()


    def modificarPorcentajeporcategoría(self,cuil,porcentaje):
        band = True
        i = 0
        aux = self.__comienzo
        while band and i < self.__tope:
            try:
                if aux.getDato().getcuil() == cuil:
                    band = False
                else:
                    i += 1
                    aux = aux.getsiguiente()
            except:
                print("cuil de agente no registrado")
                band = False
            if not band:
                sueldo = aux.getDato().getsueldoBasico() + ((aux.getDato().getantiguedad() / 100)) + (porcentaje / 100)
                round(sueldo, 2)
                aux.getDato().setsueldo(sueldo)
                aux.getDato().mostrardatos()

    def modificarImporteExtra(self,cuil,importe):
        band = True
        i = 0
        aux = self.__comienzo
        while band and i < self.__tope:
            try:
                if aux.getDato().getcuil() == cuil:
                    band = False
                else:
                    i += 1
                    aux = aux.getsiguiente()
            except:
                print("cuil de agente no registrado")
                band = False
            if not band:
                sueldo = aux.getDato().getsueldoBasico() + importe
                round(sueldo, 2)
                aux.getDato().setsueldo(sueldo)
                aux.getDato().setimporte(importe)
                aux.getDato().mostrardatos()





























