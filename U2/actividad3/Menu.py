from os import system

from claseManejador import manejador


class menu:
    __op = 0

    def __init__(self, p=0):
        self.__op = p

    def opciones(self):
        q = True
        t = manejador()
        t.cargaDatos()

        while q:
            print("\n\t --** MENÚ DE OPCIONES **--\n")
            print("1. Mostrar para cada variable el día y hora de menor y mayor valor")
            print("2. Indicar la temperatura promedio mensual por cada hora")
            print("3. Dado un número de día listar los valores de las tres variables para cada hora del día dado")
            print("4. Salir")
            self.__op = int(input("\nIndique la Opción elegida: "))
            if self.__op == 1:
                t.mayor_menor()
                system("pause")
            if self.__op == 2:
                t.promedio()
                system("pause")
            if self.__op == 3:
                t.mostrar()
                system("pause")
            if self.__op == 4:
                print('--** Gracias por utilizar nuestro sistema **--')
                q = False
                system("pause")
                system("cls")
            else:
                print('Opcion no válida, reingrese opcion')
                system("pause")
