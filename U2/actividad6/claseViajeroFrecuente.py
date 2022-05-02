class ViajeroFrecuente:
    __num_viajero = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = 0

    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def cantTotalMillas(self):
        return self.__millas_acum

    def getNombre(self):
        return self.__nombre

    def getNumViajero(self):
        return self.__num_viajero

    def __gt__(self, otro):
        return self.__millas_acum > otro.cantTotalMillas()

    def __add__(self, num: int):
        self.__millas_acum = self.__millas_acum + num
        return self

    def __sub__(self, numero: int):
        self.__millas_acum = self.__millas_acum - numero
        return self
