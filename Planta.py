from Empleado import Empleado

class Planta(Empleado):
    __basico=0.0
    __antiguedad=0

    def __init__(self,dni,nom,direc,tel,basico,antiguedad,inicio='',fin='',horas=0,valor=0.0,tarea=None,viatico=0.0,seguro=0.0):
        super().__init__(dni,nom,direc,tel,basico,antiguedad,inicio,fin,horas,valor,tarea,viatico,seguro)
        self.__basico=basico
        self.__antiguedad=antiguedad

    def getSueldo(self):
        sueldo = self.__basico + (self.__basico*self.__antiguedad)*0.01
        return sueldo
