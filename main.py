from Manejador_Personal import Coleccion_Personal
from Objerct_Encoder import ObjectEncoder
from Clase_menu import Menu
if __name__=='__main__':
    encoder = ObjectEncoder()
    Mpersonal = Coleccion_Personal()
    Mpersonal.cargararchivo(encoder)
    menu = Menu()
    menu.run(Mpersonal,encoder)

