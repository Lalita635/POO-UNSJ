from clase import Conjunto


class Controlador:
    __conjunto1: Conjunto
    __conjunto2: Conjunto

    def __init__(self):
        self.__conjunto1 = Conjunto([2, 4, 6])
        self.__conjunto2 = Conjunto([4, 8, 12])

    def mostrar(self):
        print('**-- Conjuntos --**')
        print(" A:{}\n B:{}".format(self.__conjunto1.get(), self.__conjunto2.get()))

    def union(self):
        print('**-- Unión de A y B: --**')
        union = self.__conjunto1 + self.__conjunto2
        print("{}".format(union.get()))

    def diferencia(self):
        print('**-- Diferencia entre A y B: --**')
        diferencia = self.__conjunto1 - self.__conjunto2
        print("{}".format(diferencia.get()))

    def verificacion(self):
        print('**-- Verificacion  igualdad de A y B: --**')
        verifica = self.__conjunto1 == self.__conjunto2
        if verifica:
            print("Los conjuntos son iguales")
        else:
            print("Los conjuntos son distintos")
