from menu import menu

from ManejadorPlanAhorro import manejadorPlanAhorro


if __name__ == '__main__':
    manejaPlan = manejadorPlanAhorro()
    manejaPlan.cargarObjetos()

    m = menu()
    m.get()
