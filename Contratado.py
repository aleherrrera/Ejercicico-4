from Empleado import Empleado

class Contratado(Empleado):
    __fechaInicio=''
    __fechaFin=''

    def __init__(self,dni,nom,direc,tel,basico,antiguedad,inicio,fin,horas,valor,tarea,viatico,seguro):
        super().__init__(dni,nom,direc,tel,basico,antiguedad,inicio,fin,horas,valor,tarea,viatico,seguro)
        self.__fechaInicio=inicio
        self.__fechaFin=fin

