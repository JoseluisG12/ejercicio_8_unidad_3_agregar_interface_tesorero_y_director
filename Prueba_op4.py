def ordenar_nombre(self, carrera):
    aux = self.__comienzo
    while aux is not None:
        siguiente = aux.getsiguiente()
        while siguiente is not None:
            if aux.getDato().getnombre() > siguiente.getDato().getnombre():
                if isinstance(siguiente.getDato(), Docente_Invertigador):
                    if aux.getDato().getcarrera() == carrera:
                        print("nombre ", siguiente.getDato().getnombre())
                else:
                    if isinstance(aux.getDato(), Docente_Invertigador):
                        if aux.getDato().getcarrera() == carrera:
                            print("nombre ", aux.getDato().getnombre())
                aux.getDato() == siguiente.getDato()
                siguiente.getDato() == aux.getDato()
            else:
                if isinstance(aux.getDato(), Docente_Invertigador):
                    if aux.getDato().getcarrera() == carrera:
                        print("nombre ", aux.getDato().getnombre())
            siguiente = siguiente.getsiguiente()
        aux = aux.getsiguiente()