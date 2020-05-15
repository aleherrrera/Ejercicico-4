import csv
from Tareas import Tarea

class ListaTareas:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def agregarTarea(self):
        archivo = open('tareas.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            nom = str(fila[0])
            valor = float(fila[1])
            estado = str(fila[2])
            unaTarea=Tarea(nom,valor,estado)
            self.__lista.append(unaTarea)
        archivo.close()

    def Buscar(self,nombre):
        i=0
        c=len(self.__lista)
        while i<c and nombre!=self.__lista[i].getNom():
            i+=1
        return i

    def Asignar(self, indice):
        return self.__lista[indice]

    def MostrarTarea(self):
        nombre=str(input('Ingrese nombre de la tarea: '))
        i=self.Buscar(nombre)
        if i!=None:
            if self.__lista[i].getEstado()=='no finalizado':
                print('Nombre: {}, Valor:${}'.format(self.__lista[i].getNom(),self.__lista[i].getValor()))
            else:
                print('Tarea ingresada finalizada')
        else:
            print('Nombre ingresado incorrecto')

