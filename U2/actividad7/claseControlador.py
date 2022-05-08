from claseVF import ViajeroFrecuente
import csv


class Controlador:
    __lista: list[ViajeroFrecuente]

    def __init__(self):
        self.__lista = self.getLista()

    def getLista(self):
        with open("viajeros.csv", "r") as archivo:
            contenido = csv.reader(archivo, delimiter=";")
            next(archivo)
            lista = []
            for linea in contenido:
                instancia = ViajeroFrecuente(int(linea[0]), int(linea[1]), str(linea[2]), str(linea[3]), int(linea[4]))
                lista.append(instancia)
        return lista

    def comparar(self):
        print(' **-- Comparación: --** ')
        num = int(input("Ingrese el numero de millas a comparar: "))
        print('\n**-- Comparación viajero -> numero: --**')
        for viajero in self.__lista:
            if viajero == num:
                print('Viajero: {} (Millas: {})'.format(viajero.getNombre(), viajero.cantidadTotalMillas()))

        print('\n**-- Comparación numero -> viajero: --**')
        for viajero in self.__lista:
            if num == viajero:
                print('Viajero: {} (Millas: {})'.format(viajero.getNombre(), viajero.cantidadTotalMillas()))

    def acumular(self):
        print(' **-- Acumular millas:  --** ')
        for viajero in self.__lista:
            print('Viajero: {}>Millas: {}'.format(viajero.getNombre(), viajero.cantidadTotalMillas()))
            num = int(input('Indique las millas a acumular: '))
            viajero += num
#            print('Viajero: {}>Millas: {}'.format(viajero.getNombre(), viajero.cantidadTotalMillas()))

    def canjear(self):
        print(' **-- Canjear millas: --** ')
        for viajero in self.__lista:
            print('Viajero: {}>Millas: {}'.format(viajero.getNombre(), viajero.cantidadTotalMillas()))
            num = int(input('Indique las millas a canjear: '))
            viajero -= num
#            print('Viajero: {}>Millas: {}'.format(viajero.getNombre(), viajero.cantidadTotalMillas()))

    def mostrar(self):
        i = 0
        print(' **-- VIAJEROS FRECUENTES: --** ')
        for viajeros in self.__lista:
            i += 1
            print('# Viajero: {} -> Nombre: {} -> Millas: {}'.format(i, viajeros.getNombre(), viajeros.cantidadTotalMillas()))
