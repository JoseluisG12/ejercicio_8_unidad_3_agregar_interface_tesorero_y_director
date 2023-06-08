import json
from pathlib import Path
from Manejador_Personal import Coleccion_Personal
from Clase_Docente import Docente
from Clase_Personal import Personal
from Clase_Inversitagor import  Investigador
from Clase_Docente_Investigador import Docente_Invertigador
from Clase_Personal_apollo import deApoyo
class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        else:
            return obj

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
        destino.close()

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
        fuente.close()
        return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)

    def decodificarDiccionario(self,dic, Mpersonal):
        if '__class__' not in dic:
            return dic
        else:
            class_name = dic['__class__']
            class_ = eval(class_name)
            if class_name == 'Coleccion_Personal':
                personal = dic['personal']
                Coleccion_Personal = class_()
                for i in range(len(personal)):
                    xPersonal = personal[i]
                    class_name = xPersonal.pop('__class__')
                    class_ = eval(class_name)
                    atributos = xPersonal['__atributos__']
                    unPersonal = class_(**atributos)
                    Mpersonal.agregarElemento(unPersonal)
            print('Se cargó todo el personal!')
            return Coleccion_Personal