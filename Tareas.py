class Tarea:
    __nombre=''
    __valor=0.0
    __estado=''

    def __init__(self,nombre,valor,estado):
        self.__nombre=nombre
        self.__valor=valor
        self.__estado=estado

    def getNom(self):
        return self.__nombre
    def getEstado(self):
        return self.__estado
    def getValor(self):
        return self.__valor