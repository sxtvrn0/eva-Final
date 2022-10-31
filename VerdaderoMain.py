
from docente import Docente
from estudiante import Estudiante
from nota import NotaEstudiante
from dia    import Fecha
listaDocentes=[]
listaEstudiantes=[]
ListaESTID=[]
Lista_ID_Alumno=[]
ListaCurso=[]
Lista_ID_Docente=[]
ListaAsignatura=[]


f=Fecha(21,12,2001)
#print(f.MostrarFecha())
not1=NotaEstudiante(1,4,5,6,f)
not2=NotaEstudiante(2,5,5,6,f)
not3=NotaEstudiante(3,6,5,6,f) #instanciando 5 notas Diferentes con la misma fecha para 5 alumnos diferentes
not4=NotaEstudiante(4,3,5,6,f)
not5=NotaEstudiante(5,7,5,6,f)

#print(n.mostrarNota())

est1=Estudiante(1,'alonso','1B',not1)
est2=Estudiante(2,'Bastian Riveros','1B',not2)
est3=Estudiante(3,'Juan Asunsion','1B',not3)
est4=Estudiante(4,'Felipe Filomeno','1B',not4)
est5=Estudiante(5,'Alicia Perez','1B',not5)
listaEstudiantes.append(est1)
listaEstudiantes.append(est2)
listaEstudiantes.append(est3)
listaEstudiantes.append(est4)
listaEstudiantes.append(est5)
#print(e.MostrarEstudiante())
doc1=Docente(1,'javier','Programacion',est1)
doc2=Docente(2,'alfonso','Programacion',est2) 
doc3=Docente(3,'hector','Programacion',est3) 
doc4=Docente(3,'hector','Programacion',est4) 
doc5=Docente(3,'hector','Programacion',est5) 
#print(d.MostrarDocente())
listaDocentes.append(doc1)
listaDocentes.append(doc2)
listaDocentes.append(doc3)
listaDocentes.append(doc4)
listaDocentes.append(doc5)
#e.MostrarEstudiante()
#for y in listaDocentes:
    #print('lista docente -----',y.MostrarDocente())
#for f in listaEstudiantes:
    #print('lista Estudiantes  ---',f.MostrarEstudiante())

while True:
    print('---------OPCION 1: AGREGAR DOCENTE ---------')
    print('---------OPCION 2: AGREGAR ESTUDIANTE ---------')
    print('---------OPCION 3: MODIFICAR NOTA ---------')
    print('---------OPCION 4: PROMEDIAR NOTA ---------')
    op=int(input('INGRESE UNA OPCION NUMERICA : -------'))
    if op==1:
        try:
            q=d.BuscarDocente(Id)
                idBuscar=int(input("Id Persona: "))
                q=p.buscarPersona(idBuscar,lista)
                if self.BuscarDocente==None:
                idDocente=int(input('ID DEL DOCENTE, PORFAVOR NO PONER PUNTO NI GUÍON'))
                listaDocentes.append(idDocente) #agregramos el id de docente para hacer comparacion a la hora de querer agregar un docente
                NombreDoc=input('Nombre y apellido del doctor').capitalize()
                NombreAsignatura=input('Registre las asignaturas impartidas').capitalize()
                ListaAsignatura.append(NombreAsignatura)
        except:
            print('----------DEBE INGRESAR TODOS LOS DATOS SOLICITADOS----------')
    elif op == 2:
        print('Registro de alumno  : ')
        print('Recuerde que para ingresar un Alumno primero debe ingresar fecha y nota')
        try:
            dd=int(input(' registre el dia  : '))
            mm=int(input('ingrese el mes  : '))
            aa=int(input('ingrese el año  : '))
            f=Fecha(dd,mm,aa)
            print('Debe ingresar todos los datos')
            print('Registro exitoso!, la Fecha es {} / {} / {} /'.format(dd,mm,aa))

            print('--------------------------')
            print('Ahora debes Ingresar sus Notas ')
            print('--------------------------')
            idNota=int(input('Ingrese la ID de la nota'))
            n1=int(input('Ingrese la Primera Calificacion del alumno'))
            n2=int(input('Ingrese la Segunda Calificacion del alumno'))
            n3=int(input('Ingrese la Tercerca Calificacion del alumno'))
            n=NotaEstudiante(idNota,n1,n2,n3,f)

            print('--------------------------')
            print('Ahora podra registrar al Alumno')
            print('--------------------------')
            IdAlumno=int(input('PORFAVOR INGRESE EL RUT DEL ESTUDIANTE'))
            nombre=input('Porfavor ingrese el Nombre y apellido del alumno')
            curso=input('Ingrese el curso al que pertenece')
            e=Estudiante(IdAlumno,nombre,curso,n)
            listaEstudiantes.append(e)
            d=Docente(idDocente,NombreDoc,NombreAsignatura,e)
            listaDocentes.append(d)
        except:
            print('----------DEBE INGRESAR TODOS LOS DATOS SOLICITADOS----------')

    elif op==3:
            for q in listaEstudiantes:
                print(q.MostrarEstudiante())
            IdAlumnoInt=int(input('PORFAVOR INGRESE EL ID DEL ESTUDIANTE : '))
            IdAlumnoauxiliar=""
            NombreAlumnoAux=""
            CursoAux=""
            FechaAux=""
            IdnotaAux=""
            for EstudianteF in listaEstudiantes:
                if EstudianteF.idAlumno == IdAlumnoInt:
                    IdAlumnoauxiliar=EstudianteF.idAlumno
                    NombreAlumnoAux=EstudianteF.nombre
                    IdnotaAux=EstudianteF.notaEstudiante.idNota
                    #toma el nombre asignado al id y los mantiene para guardarlos despues de editar las notas
                                                        #Cuando yo quiera eliminar una nota debo eliminar al estudiante si no me quedarian dos alumnos
                                                        #con el mismo id                                                    
                    CursoAux=EstudianteF.curso
                    FechaAux=EstudianteF.notaEstudiante.Fecha
                    print(EstudianteF.notaEstudiante.idNota)
                    print(EstudianteF.notaEstudiante.nota1)
                    print(EstudianteF.notaEstudiante.nota2)
                    print(EstudianteF.notaEstudiante.nota3)
                    print(EstudianteF.notaEstudiante.notafinal)

                    listaEstudiantes.remove(EstudianteF)
                    #print('Viendo.........')
                    #for q in listaEstudiantes:
                        #print(q.MostrarEstudiante())
                        #Remove elimina el estudiante de la lista, para poder rellenar la nota nuevamente junto con los datos del alumno
                    #asi no da problemas y no ingreso dos alumnos con el mismo id

                    print('----------------------')
                    print('Ingrese nuevas Notas  :')
                    print('----------------------')
                    n1=int(input('Ingrese nota 1------ : '))
                    n2=int(input('Ingrese nota 2------ : '))
                    n3=int(input('Ingrese nota 3------ : '))
                    nota=NotaEstudiante(IdnotaAux,n1,n2,n3,FechaAux)
                    estudianteNuevo=Estudiante(IdAlumnoauxiliar,NombreAlumnoAux,CursoAux,nota)
                    print('Id del Alumno : {}'.format(estudianteNuevo.idAlumno))
                    print('ID DE LA NOTA : {}'.format(estudianteNuevo.notaEstudiante.idNota))
                    print('PRIMERA NOTA : {}'.format(estudianteNuevo.notaEstudiante.nota1))
                    print('SEGUNDA NOTA : {}'.format(estudianteNuevo.notaEstudiante.nota2))
                    print('TERCERA NOTA : {}'.format(estudianteNuevo.notaEstudiante.nota3))
                    print('PROMEDIO FINAL DEL ALUMNO : {}'.format(estudianteNuevo.notaEstudiante.notafinal))
                    listaEstudiantes.append(estudianteNuevo)
                    for q in listaEstudiantes:
                        print(q.MostrarEstudiante())   
    elif op==4:
        #try:
            for q in listaEstudiantes:
                    print(q.MostrarEstudiante()) 
            IdAlumnoAux1=int(input('----------Ingrese el id del alumno a promediar----------'))
            for Alum in listaEstudiantes:
                #print(Alum.nombre)
                if Alum.idAlumno==IdAlumnoAux1:
                    print(Alum.nombre)
                    print(Alum.notaEstudiante.notafinal)
        #except:
           #print('error controlado------')

                
        






       









        #idDocente=int(input('porfavor ingrese el RUT, SIN PUNTO NI GUÍON'))
        #Lista_ID_Docente.append(idDocente)
        #Docente_NOMBRE = input('Ingrese el nombre y apellido del profesor')
        #listaDocentes.append(Docente_NOMBRE)
        #AsignaturaDoc=int(input('Ingrese la Asignatura'))
        #opc2=input('Quiere asignar un alumno al docente recien creado?'
            #print('EL PROFESOR DE {} ES  : {}'.format(AsignaturaDoc,Docente_NOMBRE))
            #id_estudiante=int(input('INGRESE EL RUT  :  Porfavor ingresar RUT SIN PUNTOS NI GUÍON'))
            #Lista_ID_Alumno.append(id_estudiante)
            #NombreAlum=input('Ingrese el nombre del estudiante')
            #listaEstudiantes.append(NombreAlum)
           # opc3=input('Desea terminar?')
    