from Empleado import Empleado

class Externo(Empleado):
    __tarea=''
    __inicio=''
    __fin=''
    __viatico=0.0
    __costo=0.0
    __seguroVida=0.0

    def __init__(self,dni,nom,direc,tel,inicio,fin,tarea,viatico,costo,seguro,basico=0.0,antiguedad=0,horas=0,valor=0.0):
        super().__init__(dni,nom,direc,tel,basico,antiguedad,inicio,fin,horas,valor,tarea,viatico,costo,seguro)
        self.__tarea=tarea
        self.__inicio=inicio
        self.__fin=fin
        self.__viatico=viatico
        self.__costo=costo
        self.__seguroVida=seguro

    def getSueldo(self):
        sueldo = self.__costo - (self.__viatico+self.__seguroVida)
        return sueldo
    def getTarea(self):
        return self.__tarea
    def getFin(self):
        return self.__fin
    def getCosto(self):
        return self.__costo