class Empleado:
    __dni=0
    __nombre=''
    __direccion=''
    __telefono=''

    def __init__(self,dni,nom,direc,tel,basico,antiguedad,inicio,fin,horas,valor,tarea,viatico,costo,seguro):
        self.__dni=dni
        self.__nombre=nom
        self.__direccion=direc
        self.__telefono=tel

    def getDni(self):
        return self.__dni
    def getNom(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono

    def __str__(self):
        cadena='%s %d %s'%(self.__nombre,self.__dni,self.__direccion)
        return cadena