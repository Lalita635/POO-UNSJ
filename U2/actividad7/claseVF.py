from __future__ import annotations


class ViajeroFrecuente:
    __num_viajero: int
    __dni: int
    __nombre: str
    __apellido: str
    __millas_acum: int

    def __init__(self, num=0, dni=0, nom='', ap='', acum=0):
        self.__num_viajero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millas_acum = acum

    def getNombre(self):
        return self.__nombre

    def cantidadTotalMillas(self):
        return self.__millas_acum

    def canjearMillas(self, canjear):
        if canjear <= self.__millas_acum:
            self.__millas_acum = self.__millas_acum - canjear
            return self.__millas_acum
        else:
            print("Error de Operacion")

    def modificar(self, v):
        self.__millas_acum = v
        return self.__millas_acum

    def __gt__(self, viajero: ViajeroFrecuente):
        return self.__millas_acum > viajero.cantidadTotalMillas()

    def __add__(self, n: int):
        self.__millas_acum = self.__millas_acum + n
        return self

    def __sub__(self, o: int):
        self.__millas_acum = self.__millas_acum - o
        return self

    def __eq__(self, otro: int):
        return self.__millas_acum == otro

    def __req__(self, otro: int):
        return otro == self.__millas_acum

    def __radd__(self, numero: int):
        self.__millas_acum = numero + self.__millas_acum
        return self

    def __rsub__(self, numero: int):
        self.__millas_acum = numero - self.__millas_acum
        self.__millas_acum = self.__millas_acum * (-1)
        return self
