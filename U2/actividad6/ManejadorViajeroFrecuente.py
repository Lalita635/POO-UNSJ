import csv
from claseViajeroFrecuente import ViajeroFrecuente


class manejadorVF:
    __lista: list[ViajeroFrecuente]

    def __init__(self):
        self.__lista = self.cargarObjeto()

    def cargarObjeto(self):
        listaViajero = []
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            v = ViajeroFrecuente(int(fila[0]), int(fila[1]), str(fila[2]), str(fila[3]), int(fila[4]))
            listaViajero.append(v)
        archivo.close()
        return listaViajero

    #1
    def compara(self):
        MAX = self.__lista[0]
        for viajero in self.__lista:
            if viajero > MAX:
                MAX = viajero
        print("Viajeros con mayor cantidad de millas acumuladas")
        for viajero in self.__lista:
            if MAX.cantTotalMillas() == viajero.cantTotalMillas():
                print("Viajero: {} - Nombre: {} - Millas: {}".format(viajero.getNumViajero(), viajero.getNombre(), viajero.cantTotalMillas()))

    #2
    def acumula(self):
        for viajero in self.__lista:
            num = int(input("Millas actuales: {} --- Ingrese millas a acumular: ".format(viajero.cantTotalMillas())))
            viajero += num
            print("Nueva cantidad de millas acumuladas: {}".format(viajero.cantTotalMillas()))

    #3
    def canjea(self):
        for viajero in self.__lista:
            num = int(input("Millas actuales: {} --- Ingrese millas a canjear: ".format(viajero.cantTotalMillas())))
            viajero -= num
            print("Nueva cantidad de millas: {}".format(viajero.cantTotalMillas()))
