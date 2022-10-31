class NotaEstudiante():
    def __init__(self,idNota,n1,n2,n3,Fecha):
        self.idNota=idNota
        self.nota1=n1
        self.nota2=n2
        self.nota3=n3
        self.notafinal=[]
        self.Fecha=Fecha
    def mostrarNota(self):
        return "\nId Nota  : "+str(self.idNota)+\
                "\nCalificacion 1 : "+str(+self.nota1)+\
                "\nCalificacion 2 : "+str(self.nota2)+\
                "\nCalificacion 3 : "+str(self.nota3)+\
                "\nCalificacion Final  : "+str(self.notafinal)+\
                "\nFecha  : "+self.Fecha.MostrarFecha()

                
                