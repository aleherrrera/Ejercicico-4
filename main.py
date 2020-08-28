from tkinter import *
from tkinter import ttk
from functools import partial
from Fraccion import Fraccion

class Calculadora(object):
    __ventana = None
    __operador = None
    __panel = None
    __operadorAux = None
    __primerOperando = None
    __segundoOperando = None
    __primerFraccion= None
    __segundaFraccion = None
    __bandera= False

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador = StringVar()
        self.__operadorAux = None
        operatorEntry = ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W, E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right', state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO, '2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO, '3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO, '4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO, '5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO, '6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO, '7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO, '8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO, '9')).grid(column=3, row=5, sticky=W)
        ttk.Entry(mainframe, width=10, justify='center', state='disabled').grid(column=1, row=6, sticky=(W, E))
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=2, row=6, sticky=W)
        ttk.Entry(mainframe, width=10, justify='center', state='disabled').grid(column=3, row=6, sticky=(W, E))
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=7, sticky=W)
        ttk.Button(mainframe, text='/', command=self.cambio).grid(column=1, row=8, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=3, row=8, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=2, row=8, sticky=W)
        ttk.Button(mainframe, text='C', command=self.limpiar).grid(column=2, row=9, sticky=W)

        self.__panel.set('')
        panelEntry.focus()
        self.__ventana.mainloop()

    def ponerNUMERO(self, numero):
        if self.__bandera == True:
            self.fraccion(numero)
        else:
            if self.__operadorAux == None:
                # forma numeros de mas de una cifra
                valor = self.__panel.get()
                self.__panel.set(valor + numero)
            else:
                # si se ingreso un operador se guarda el valor del panel como primer operando
                # luego el operador es = NONE y el nuevo numero ingresado se pasa al panel para formar el
                # segundo operando
                print('a')
                self.__operadorAux = None
                valor = self.__panel.get()
                self.__primerOperando = valor
                self.__panel.set(numero)

    def resolverOperacion(self, operando1, operacion, operando2):
        resultado = 0
        if operacion == '+':
            resultado = operando1 + operando2
        else:
            if operacion == '-':
                resultado = operando1 - operando2
            else:
                if operacion == '*':
                    resultado = operando1 * operando2
                else:
                    if operacion == '%':
                        resultado = operando1 / operando2
        self.__panel.set(str(resultado))

    def ponerOPERADOR(self, op):
        # si el operador es '=' se resuelve la operacion
        if op == '=':
            if self.__primerFraccion == None:
                operacion = self.__operador.get()
                self.__segundoOperando = int(self.__panel.get())
                self.resolverOperacion(int(self.__primerOperando), operacion, self.__segundoOperando)
                self.__operador.set('')
                self.__operadorAux = None
            else:
                operacion = self.__operador.get()
                self.__primerOperando = self.__primerFraccion
                self.__segundoOperando = self.__segundaFraccion
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set('')
                self.__operadorAux = None
        else:
            #si el operador esta vacio se guarda el operador ingresado
            if self.__operador.get() == '':
                self.__operador.set(op)
                self.__operadorAux = op
            else:
                # si el operador no es '=' y tampoco esta vacio es porque se siguen cargando numeros
                # y operaciones que se iran resolviendo automaticamente
                operacion = self.__operador.get()
                self.__segundoOperando = int(self.__panel.get())
                self.resolverOperacion(int(self.__primerOperando), operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux = op

    def fraccion(self,numero):
        n = int(numero)
        if self.__primerFraccion == None:
            valor = int(self.__panel.get())
            self.__primerFraccion = Fraccion(valor, n)
            self.__panel.set(self.__primerFraccion)
            self.__primerOperando=None
            self.__bandera=False
        else:
            valor = int(self.__panel.get())
            self.__segundaFraccion=Fraccion(valor,n)
            self.__panel.set(self.__segundaFraccion)
            self.__primerOperando=None
            self.__bandera = False

    def cambio(self):
        self.__bandera=True

    def limpiar(self):
        self.__panel.set(0)
        self.__primerOperando=None
        self.__segundoOperando=None
        self.__primerFraccion=None
        self.__segundaFraccion=None
        self.__operador.set('')
        self.__operadorAux = None

def main():
    calculadora = Calculadora()

if __name__ == '__main__':

    main()

