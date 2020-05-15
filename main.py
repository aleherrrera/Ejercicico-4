from ColeccionEmpleados import ArregloEmpleados
from ManejadorPlanta import ListaPlanta
from ManejadorInterno import ListaInterno
from ManejadorExterno import ListaExterno
from ManejadorTarea import ListaTareas

def opcion0():
    print("Adiós")

def opcion1():
    Empleados.RegistrarHoras()

def opcion2():
    Tareas.MostrarTarea()

def opcion3():
    Empleados.Ayuda()

def opcion4():
    Empleados.MostrarSueldos()

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':

    Empleados = ArregloEmpleados(6)
    Plantas = ListaPlanta()
    Internos = ListaInterno()
    Externos = ListaExterno()
    Tareas = ListaTareas()

    Tareas.agregarTarea()
    Plantas.agregarPlanta()
    Internos.agregarInterno()
    Externos.agregarExterno(Tareas)

    c=Plantas.Cant()
    Empleados.CargarEmpleados(Plantas,c)
    c=Internos.Cant()
    Empleados.CargarEmpleados(Internos,c)
    c=Externos.Cant()
    Empleados.CargarEmpleados(Externos,c)

    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print("0. Salir")
        print("1. Registrar horas")
        print("2. Total de tarea")
        print("3. Ayuda")
        print('4. Mostrar sueldo')
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú

