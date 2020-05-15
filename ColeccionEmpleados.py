import numpy as np
from Empleado import Empleado

class ArregloEmpleados:
    __cantidad=0
    __dimension=0

    def __init__(self,dimension):
        self.__empledados=np.empty(dimension,dtype=Empleado)
        self.__cantidad=0
        self.__dimension=dimension

    def CargarEmpleados(self,lista,c):
        if self.__cantidad<self.__dimension:
            for i in range(c):
                self.__empledados[self.__cantidad]=lista.Asignar(i)
                print(self.__empledados[self.__cantidad])
                self.__cantidad+=1

    def Buscar(self,dni):
        i=0
        while i<self.__cantidad and dni!=self.__empledados[i].getDni():
            i+=1
        return i

    def RegistrarHoras(self):
        dni = int(input('Ingrese DNI de empleado contratado interno: '))
        i=self.Buscar(dni)
        if i != None:
            print('Horas: {}'.format(self.__empledados[i].getHoras()))
            horas=int(input('Ingresar cantidad de horas: '))
            self.__empledados[i].setHoras(horas)
            print('Horas: {}'.format(self.__empledados[i].getHoras()))
        else:
            print('DNI ingresado incorrecto')

    def Ayuda(self):
        print('Nombre      Direccion      Dni')
        for i in range(self.__cantidad):
            if self.__empledados[i].getSueldo()<25000:
                print(self.__empledados[i])

    def MostrarSueldos(self):
        print('Nombre    Telefono    Sueldo')
        for i in range(self.__cantidad):
                print('{}    {}    ${}'.format(self.__empledados[i].getNom(),self.__empledados[i].getTelefono(),self.__empledados[i].getSueldo()))
