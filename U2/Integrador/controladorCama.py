import csv
import numpy as np

from claseCama import Cama


class ControladorCama:
    __array = []

    def __init__(self):
        self.__array = []

    def cargarCama(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo, delimiter=';')
        ban = True
        nuevo = np.array([Cama()]*30)

        for fila in reader:
            if ban:
                ban = not ban
            else:
                cama = Cama(int(fila[1]), bool(fila[2]), str(fila[3]), str(fila[4]), str(fila[5]), str(fila[6]))
                if int(fila[0]) != 0:
                    nuevo[int(fila[0])-1] = cama
        self.__array = nuevo

    def ListaPacienteAlta(self):
        p = input("Ingrese el Apellido y Nombre del paciente: ")
        i = 0
        while i < 30 and p != self.__array[i].getNombreyApellido():
            i += 1
        if i == 30:
            print("Paciente no encontrado!")
        else:
            print("Paciente: {}  Cama: {} Habitaciòn: {}".format(self.__array[i].getNombreyApellido(), i+1, self.__array[i].getHabitacion()))
            print("Diagnòstico: {}  Fecha de Internacion: {}".format(self.__array[i].getDiagnostico(), self.__array[i].getFechInternacion()))
            p = int(input('Desea dar de alta? 1.SI 2.NO: '))
            if p == 1:
                self.__array[i].ModificarFechAlta()
                print("Fecha de Alta : {}".format(self.__array[i].getFechAlta()))
            else:
                print('El paciente continua internado!')
        return i

    def ListaPacienteInternado(self):
        q = input('Ingrese un diagnóstico: ')
        for i in range(30):
            if self.__array[i].getEstado() and q == self.__array[i].getDiagnostico():
                print("Habitación: {}\nPaciente: {}\nFecha de Internación: {}".format(self.__array[i].getHabitacion(), self.__array[i].getNombreyApellido(), self.__array[i].getFechInternacion(), self.__array[i].getFechAlta()))
