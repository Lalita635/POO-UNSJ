from clasePlanAhorro import PlanAhorro
import csv


class manejadorPlanAhorro:
    __listaObjetos: list[PlanAhorro]

    def __init__(self):
        self.__listaObjetos = []

    def cargarObjetos(self):
        with open('Planes.csv', 'r', encoding='utf8') as archivo:
            reader = csv.reader(archivo, delimiter=',')
            for t in reader:
                objeto = PlanAhorro(int(t[0]), str(t[1]), str(t[2]), int(t[3]))
                PlanAhorro.modificaCuotas(int(t[4]))
                PlanAhorro.modificaLicitar(int(t[5]))
                self.__listaObjetos.append(objeto)

    def modificar(self):
        for obj in self.__listaObjetos:
            obj.mostrar()
            nuevo = int(input('Ingrese el nuevo valor del vehículo: '))
            obj.modificaPrecio(nuevo)

    def mostrarDatos(self):
        valor = int(input('Ingrese valor :'))
        for ob in self.__listaObjetos:
            valorCuota: float = (ob.getPrecio()/ob.getCuotas()) + ob.getPrecio() * 0.1
            if valor > valorCuota:
                ob.mostrar()

    def mostrarMonto(self):
        for o in self.__listaObjetos:
            print('Plan: ' + str(o.getCodigo()))
            valorCta: float = (o.getPrecio() / o.getCuotas()) + o.getPrecio() * 0.1
            monto: float = valorCta * o.getLicitar()
            print('Monto que debe haber pagado para licitar: ' + str(monto))

    def modificarCoutas(self):
        cant = int(input('Ingrese la cantidad nueva de cuotas: '))
        PlanAhorro.modificaLicitar(cant)
        print('Cantidad de cuotas modificadas!')
