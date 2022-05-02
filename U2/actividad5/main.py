from menu import menu

from ManejadorPlanAhorro import manejadorPlanAhorro


if __name__ == '__main__':
    manejaPlan = manejadorPlanAhorro()
    manejaPlan.cargarObjetos()
    opc = 0
    m = menu()
    while opc != 6:
        m.mostrar()
        opc = int(input('Ingrese la opción elegida: '))
        menu.opciones(opc)
