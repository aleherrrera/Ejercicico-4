import csv
from datetime import datetime
import numpy as np
from Empleado import Empleado
from Externo import Externo
from Planta import Planta
from Contratado import Contratado

class ArregloEmpleados:
    __cantidad=0
    __dimension=0
    __incremento=2

    def __init__(self,dimension,incremento=2):
        self.__empledados=np.empty(dimension,dtype=Empleado)
        self.__cantidad=0
        self.__dimension=dimension

    def cargaExterno(self):
        if self.__cantidad==self.__dimension:
            self.__dimension += self.__incremento
            self.__empledados.resize(self.__dimension)
        archivo = open('externos.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            dni = int(fila[0])
            nom = str(fila[1])
            direc = str(fila[2])
            telef = str(fila[3])
            inicio = str(fila[4])
            fin = str(fila[5])
            tarea = str(fila[6])
            viatico = float(fila[7])
            costo = float(fila[8])
            seguro = float(fila[9])
            unEmpleado = Externo(dni, nom, direc, telef, inicio, fin, tarea, viatico, costo, seguro)
            self.__empledados[self.__cantidad]=unEmpleado
            print(self.__empledados[self.__cantidad])
            self.__cantidad += 1
        archivo.close()

    def cargaPlanta(self):
        if self.__cantidad==self.__dimension:
            self.__dimension += self.__incremento
            self.__empledados.resize(self.__dimension)
        archivo = open('planta.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            dni = int(fila[0])
            nom = str(fila[1])
            direc = str(fila[2])
            tel = str(fila[3])
            basico = float(fila[4])
            antiguedad = int(fila[5])
            unEmpleado = Planta(dni, nom, direc, tel, basico, antiguedad)
            self.__empledados[self.__cantidad]=unEmpleado
            print(self.__empledados[self.__cantidad])
            self.__cantidad += 1
        archivo.close()

    def cargarContratado(self):
        if self.__cantidad==self.__dimension:
            self.__dimension += self.__incremento
            self.__empledados.resize(self.__dimension)
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
            self.__empledados[self.__cantidad] = unEmpleado
            print(self.__empledados[self.__cantidad])
            self.__cantidad += 1
        archivo.close()

    def Buscar(self,dni):
        i=0
        while i<self.__cantidad and dni!=self.__empledados[i].getDni():
            i+=1
        return i

    def RegistrarHoras(self):
        dni = int(input('Ingrese DNI de el empleado contratado: '))
        i=self.Buscar(dni)
        if i != None:
            print('Horas: {}'.format(self.__empledados[i].getHoras()))
            horas=int(input('Ingresar cantidad de horas: '))
            self.__empledados[i].setHoras(horas)
            print('Horas: {}'.format(self.__empledados[i].getHoras()))
        else:
            print('DNI ingresado incorrecto')

    def BuscarTarea(self,nom):
        i=0
        while i<self.__cantidad and nom!=self.__empledados[i].getTarea():
            i+=1
        return i

    def Tarea(self):
        nom=str(input('Ingresar nombre de la tarea: '))
        i=self.BuscarTarea(nom)
        if i != None:
            fin=self.__empledados[i].getFin()
            now = datetime.now()
            hoy=now.strftime('%Y-%m-%d')
            if hoy<fin:
                 print('Tarea: {}\nCosto: ${}'.format(self.__empledados[i].getTarea(),self.__empledados[i].getCosto()))
            else:
                print('La tarea ya finalizó')

    def Ayuda(self):
        print('Nombre     Dni    Direccion')
        for i in range(self.__cantidad):
            if self.__empledados[i].getSueldo()<25000:
                print(self.__empledados[i])

    def MostrarSueldos(self):
        print('Nombre    Telefono    Sueldo')
        for i in range(self.__cantidad):
                print('{}    {}    ${}'.format(self.__empledados[i].getNom(),self.__empledados[i].getTelefono(),self.__empledados[i].getSueldo()))
