import csv
from Externo import Externo

class ListaExterno:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def agregarExterno(self,Tarea):
        archivo = open('externos.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            dni = int(fila[0])
            nom = str(fila[1])
            direc = str(fila[2])
            telef = str(fila[3])
            inicio = str(fila[4])
            fin = str(fila[5])
            nomtarea=str(fila[6])
            viatico = float(fila[7])
            seguro = float(fila[8])
            i=Tarea.Buscar(nomtarea)
            tarea=Tarea.Asignar(i)
            unEmpleado=Externo(dni,nom,direc,telef,inicio,fin,tarea,viatico,seguro)
            self.__lista.append(unEmpleado)
        archivo.close()

    def Cant(self):
        return len(self.__lista)

    def Asignar(self, indice):
        return self.__lista[indice]