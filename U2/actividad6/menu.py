from ManejadorViajeroFrecuente import manejadorVF
from os import system


class Menu:
    __op: int

    def __init__(self):
        self.__op = 0

    def get(self):
        q = True
        n = manejadorVF()
        n.cargarObjeto()

        while q:
            print("\n\t --** MENÚ DE OPCIONES **--\n")
            print("1. Mostrar el/los viajeros con mayor cantidad de millas acumuladas:")
            print("2. Acumular millas")
            print("3. Canjear millas")
            print("4. Salir")
            self.__op = int(input("\nIndique la Opción elegida: "))
            if self.__op == 1:
                n.compara()
                system("pause")
            if self.__op == 2:
                n.acumula()
                system("pause")
            if self.__op == 3:
                n.canjea()
                system("pause")
            if self.__op == 4:
                print('--** Gracias por utilizar nuestro sistema **--')
                q = False
                system("pause")
                system("cls")
            else:
                print('Opcion no válida, reingrese opcion')
                system("pause")
