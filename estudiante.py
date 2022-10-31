
from nota import NotaEstudiante


class Estudiante():
    def __init__(self,idAlumno,nombre,curso,notaEstudiante):
        self.idAlumno=idAlumno
        self.nombre=nombre
        self.curso=curso
        self.notaEstudiante=notaEstudiante
    def MostrarEstudiante(self):
        return "\nID Alumno  : "+str(self.idAlumno)+\
                "\nNombre  :  "+self.nombre+\
                "\nCurso  : " +self.curso+\
                self.notaEstudiante.mostrarNota()


     #def AgregarEstudiante(self,idNuevo,listaEstudiantes,Nombre,curso,NotaEstudiante):

            #NombreDoc = input('Nombrese ---------')
            #curso = input('escriba su asignatura -------')
            #NotaEstudiante = n
            #e=Estudiante(idNuevo,Nombre,NombreAsignatura,Estudiante)
            #listaEstudiantes.append(d)
            #pass

