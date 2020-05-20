import csv
from Externo import Externo
from datetime import datetime

class ListaExterno:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def agregarExterno(self):
        archivo = open('externos.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            dni = int(fila[0])
            nom = str(fila[1])
            direc = str(fila[2])
            telef = str(fila[3])
            inicio = str(fila[4])
            fin = str(fila[5])
            tarea=str(fila[6])
            viatico = float(fila[7])
            costo= float(fila[8])
            seguro = float(fila[9])
            unEmpleado=Externo(dni,nom,direc,telef,inicio,fin,tarea,viatico,costo,seguro)
            self.__lista.append(unEmpleado)
        archivo.close()

    def Cant(self):
        return len(self.__lista)

    def Asignar(self, indice):
        return self.__lista[indice]

    def BuscarTarea(self,nom):
        i=0
        c=self.Cant()
        while i<c and nom!=self.__lista[i].getTarea():
            i+=1
        if i < c:
            return i

    def Tarea(self):
        nom=str(input('Ingresar nombre de la tarea: '))
        i=self.BuscarTarea(nom)
        if i != None:
            fin=self.__lista[i].getFin()
            now = datetime.now()
            hoy=now.strftime('%Y-%m-%d')
            if hoy<fin:
                 print('Tarea: {}\nCosto: ${}'.format(self.__lista[i].getTarea(),self.__lista[i].getCosto()))
            else:
                print('La tarea ya finalizó')
        else:
            print('Nombre de tarea incorrecto')