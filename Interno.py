from Contratado import Contratado

class Interno(Contratado):
    __horas=0
    __valorHora=0.0

    def __init__(self,dni,nom,direc,tel,inicio,fin,horas,valor,basico=0.0,antiguedad=0,tarea=None,viatico=0.0,seguro=0.0):
        super().__init__(dni,nom,direc,tel,basico,antiguedad,inicio,fin,horas,valor,tarea,viatico,seguro)
        self.__horas=horas
        self.__valorHora=valor

    def getHoras(self):
        return self.__horas
    def setHoras(self,horas):
        self.__horas+=horas

    def getSueldo(self):
        sueldo = self.__horas * self.__valorHora
        return sueldo
