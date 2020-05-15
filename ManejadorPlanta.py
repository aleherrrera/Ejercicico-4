import csv
from Planta import Planta

class ListaPlanta:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def agregarPlanta(self):
        archivo=open('planta.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            dni=int(fila[0])
            nom=str(fila[1])
            direc=str(fila[2])
            tel=str(fila[3])
            basico=float(fila[4])
            antiguedad=int(fila[5])
            unEmpleado=Planta(dni,nom,direc,tel,basico,antiguedad)
            self.__lista.append(unEmpleado)
        archivo.close()

    def Cant(self):
        return len(self.__lista)

    def Asignar(self,indice):
        return self.__lista[indice]