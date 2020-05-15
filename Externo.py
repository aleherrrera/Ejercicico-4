from Contratado import Contratado
from Tareas import Tarea

class Externo(Contratado):
    __viatico=0.0
    __seguroVida=0.0
    __tarea=Tarea

    def __init__(self,dni,nom,direc,tel,inicio,fin,tarea,viatico,seguro,basico=0.0,antiguedad=0,horas=0,valor=0.0):
        super().__init__(dni,nom,direc,tel,basico,antiguedad,inicio,fin,horas,valor,tarea,viatico,seguro)
        self.__viatico=viatico
        self.__seguroVida=seguro
        self.__tarea=tarea

    def getSueldo(self):
        sueldo = self.__tarea.getValor() - (self.__viatico+self.__seguroVida)
        return sueldo