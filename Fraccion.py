class Fraccion:
    __num=0
    __den=1

    def __init__(self, n, d):
        self.__num = n
        self.__den = d

    def __add__(self, otraFraccion):
        nuevoNum = self.__num * otraFraccion.__den + self.__den * otraFraccion.__num
        nuevoDen = self.__den * otraFraccion.__den
        comun = self.mcd(nuevoNum, nuevoDen)
        return Fraccion(nuevoNum // comun, nuevoDen // comun)

    def __sub__(self, otraFraccion):
        nuevoNum = self.__num * otraFraccion.__den - self.__den * otraFraccion.__num
        nuevoDen = self.__den * otraFraccion.__den
        comun = self.mcd(nuevoNum, nuevoDen)
        return Fraccion(nuevoNum // comun, nuevoDen // comun)

    def __mul__(self, otraFraccion):
        nuevoNum = self.__num * otraFraccion.__num
        nuevoDen = self.__den * otraFraccion.__den
        comun = self.mcd(nuevoNum, nuevoDen)
        return Fraccion(nuevoNum // comun, nuevoDen // comun)

    def __truediv__(self, otraFraccion):
        nuevoNum = self.__num * otraFraccion.__den
        nuevoDen = self.__den * otraFraccion.__num
        comun = self.mcd(nuevoNum, nuevoDen)
        return Fraccion(nuevoNum // comun, nuevoDen // comun)

    def num(self):
        return self.__den

    def mcd(self, m, n):
        while m % n != 0:
            mViejo = m
            nViejo = n

            m = nViejo
            n = mViejo % nViejo
        return n

    def __str__(self):
        if self.__num==self.__den:
            return str(1)
        return str(self.__num) +'/'+ str(self.__den)
