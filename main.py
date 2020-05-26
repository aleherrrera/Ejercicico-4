from ColeccionEmpleados import ArregloEmpleados

def opcion0():
    print("Adiós")

def opcion1():
    Empleados.RegistrarHoras()

def opcion2():
    Empleados.Tarea()

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

    Empleados.cargaExterno()
    Empleados.cargaPlanta()
    Empleados.cargarContratado()

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