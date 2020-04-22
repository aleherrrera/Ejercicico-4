
class FechaHora:

    __dia = 0
    __mes = 0
    __anio = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__(self,dia=1,mes=1,anio=2020,hora=0,minuto=0,segundo=0):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.__hora = hora
        self.__minutos = minuto
        self.__segundos = segundo

    def Mostrar(self):
        s = 'DIA/MES/AÑO    HORA:MIN:SEG\n'
        print('{}{}/{}/{}          {}:{}:{}'.format(s,self.__dia,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos))

    def Bisiesto(self,anio):
        m = anio%4
        if m == 0:
            m = anio%100
            if m == 0:
                m = anio%400
                if m == 0:
                    return 29
                else:
                    return 28

    def Mes(self,mes):
        if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            return 31
        if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            return 30
        else:
            a = self.Bisiesto(self.__anio)
            return a

    def PonerEnHora(self,hora=0,min=0,seg=0):
        self.__hora = hora
        self.__minutos = min
        self.__segundos = seg

    def AdelantarHora(self,hora=0,min=0,seg=0):
        s = self.__segundos + seg
        if s > 59:
            self.__segundos = s - 60
            self.__minutos += 1
        else:
            self.__segundos = s

        m = self.__minutos + min
        if m > 59:
            self.__minutos = m - 60
            self.__hora += 1
        else:
            self.__minutos = m

        h = hora + self.__hora
        if h > 23:
            self.__hora = h - 24
            self.__dia += 1
            m = self.Mes(self.__mes)
            if self.__dia > m:
                self.__mes += 1
                if self.__mes > 12:
                    self.__anio += 1
        else:
            self.__hora = h


