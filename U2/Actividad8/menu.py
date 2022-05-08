import os
from controlador import Controlador


class Menu:
    __opcion: int
    __control: Controlador

    def __init__(self):
        self.__opcion = 0
        self.__control = Controlador()

    def get(self):
        centinela = 0
        while centinela == 0:
            print('\n\t **-- MENU --++')
            print('\tSeleccione la opción deseada: ')
            print(' 1. Cargar conjuntos A y B')
            print(' 2. Mostrar conjuntos A y B')
            print(' 3. A unión B')
            print(' 4. A diferencia B')
            print(' 5. Son A y B iguales?')
            print(' 6. Salir \n')
            self.__opcion = int(input('Opcion: '))

            if self.__opcion == 1:
                print('Conjuntos cargados!')
                os.system("pause")
                os.system("cls")

            if self.__opcion == 2:
                self.__control.mostrar()
                os.system("pause")

            if self.__opcion == 3:
                self.__control.union()
                os.system("pause")

            if self.__opcion == 4:
                os.system("cls")
                self.__control.diferencia()
                os.system("pause")

            if self.__opcion == 5:
                os.system("cls")
                self.__control.verificacion()
                os.system("pause")

            else:
                os.system("cls")
                print("\t Saliendo...")
                centinela = 1
