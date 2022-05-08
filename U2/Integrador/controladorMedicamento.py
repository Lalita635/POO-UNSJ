import csv
from claseMedicamento import Medicamento


class ControladorMedicamento:
    __medicamento = []

    def __init__(self):
        self.__medicamento = None

    def CargaMedicamento(self):
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter=';')
        medicamentos = []
        ban = True
        for fila in reader:
            if ban:
                ban = not ban
            else:
                med = Medicamento(int(fila[0]), int(fila[1]), str(fila[2]), str(fila[3]), str(fila[4]), int(fila[5]), float(fila[6]))
                medicamentos.append(med)
        self.__medicamento = medicamentos

    def BuscarMedicamento(self, IdCama):
        cant = 0
        print("Medicamento/Monodroga        Presentacion          Cantidad               Precio")
        for i in range(len(self.__medicamento)):
            if self.__medicamento[i].getIdCama2() == IdCama:
                cant += self.__medicamento[i].getCantidadAplicada()
                print("{}/{}           {}                {}                  {}".format(self.__medicamento[i].getNombreComercial(), self.__medicamento[i].getMonodroga(), self.__medicamento[i].getPresentacion(), self.__medicamento[i].getCantidadAplicada(), self.__medicamento[i].getPrecioTotal()*self.__medicamento[i].getCantidadAplicada()))
                j = i
        print('Total Adeudado: {} '.format(cant * self.__medicamento[j].getPrecioTotal()))
