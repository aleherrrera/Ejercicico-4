import csv
from Contratado import Contratado

class ListaContratado:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def agregarContratado(self):
        archivo = open('contratados.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            dni = int(fila[0])
            nom = str(fila[1])
            direc = str(fila[2])
            tel = str(fila[3])
            inicio= str(fila[4])
            fin = str(fila[5])
            horas = int(fila[6])
            valor = float(fila[7])
            unEmpleado=Contratado(dni,nom,direc,tel,inicio,fin,horas,valor)
            self.__lista.append(unEmpleado)
        archivo.close()

    def Cant(self):
        return len(self.__lista)

    def Asignar(self, indice):
        return self.__lista[indice]