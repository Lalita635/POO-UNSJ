import os
from controladorCama import ControladorCama
from controladorMedicamento import ControladorMedicamento


class menu:
    __opcion: int

    def __init__(self, op=0):
        self.__opcion = op

    def getmenu(self):
        corte = 0
        while corte == 0:
            print('\n\t **-- MENU --++')
            print('\tSeleccione la opción deseada: ')
            print(' 1. Listar pacientes de alta:')
            print(' 2. Listar pacientes internados:')
            print(' 3. Salir \n')
            self.__opcion = int(input('Opcion: '))

            if self.__opcion == 1:
                c = ControladorCama()
                c.cargarCama()
                pos = c.ListaPacienteAlta()
                if pos < 30:
                    c = ControladorMedicamento()
                    c.CargaMedicamento()
                    c.BuscarMedicamento(pos+1)
                os.system('pause')

            if self.__opcion == 2:
                c = ControladorCama()
                c.cargarCama()
                c.ListaPacienteInternado()
                os.system('pause')

            if self.__opcion == 3:
                print("\t Saliendo...")
                corte = 1
                os.system('pause')

            else:
                print('Opción no válida')
