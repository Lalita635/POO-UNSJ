import os
from claseControlador import Controlador


class menu:
    __opcion: int
    __control: Controlador

    def __init__(self):
        self.__opcion = 0
        self.__control = Controlador()

    def get(self):
        ban = True
        while ban:
            print('\n\t **-- MENU --++')
            print('\tSeleccione la opción deseada: ')
            print(' 1. Mostrar listado de Viajeros Frecuentes')
            print(' 2. Comparar millas acumuladas')
            print(' 3. Acumular millas')
            print(' 4. Canjear millas')
            print(' 5. Salir \n')
            self.__opcion = int(input('Opcion: '))

            if self.__opcion == 1:
                self.__control.mostrar()
                os.system('pause')

            if self.__opcion == 2:
                self.__control.comparar()
                os.system("pause")

            if self.__opcion == 3:
                self.__control.acumular()
                os.system("pause")

            if self.__opcion == 4:
                self.__control.canjear()
                os.system("pause")

            if self.__opcion == 5:
                print("\t Saliendo...")
                ban = False
            else:
                print('Opción no válida, presiones enter para ingresar al menu nuevamente')
                os.system('pause')
