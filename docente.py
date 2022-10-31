from estudiante import Estudiante


class Docente():
    def __init__(self,idDocente,NombreDoc,NombreAsignatura,Estudiante):
        self.idDocente=idDocente
        self.NombreDoc=NombreDoc
        self.NombreAsignatura=NombreAsignatura
        self.Estudiante=Estudiante
        
    def MostrarDocente(self):
        return "\nID Docente  : "+str(self.idDocente)+\
                "\nNombre  :  "+self.NombreDoc+\
                "\nAsignatura  : "+self.NombreAsignatura+\
                self.Estudiante.MostrarEstudiante()
        
    def BuscarDocente(self,idBuscar,listaDocentes):
        for q in listaDocentes:
            if idBuscar == q.idDocente:
                return q
        return None


    def AgregarDocente(self,idNuevo,listaDocentes):
            NombreDoc = input('Nombrese ---------')
            NombreAsignatura = input('escriba su asignatura -------')
        
    




    def MostrarListaDocente(self,listaDocentes):
        for lis in listaDocentes:
            print(lis.MostrarDocente())
