from os import system

from claseListaViajeros import ListaViajeros

def menu():
    viajero = listaViajeros.getViajero(num)
    while True:
        print("\n--** MENÚ DE OPCIONES **--\n")
        print("Viajero seleccionado: {}\n".format(viajero))
        print("1. Consultar cantidad de millas")
        print("2. Acumular millas")
        print("3. Canjear millas")
        print("4. Salir")
        opc = int(input("\nIndique la Opción elegida: "))
        if opc == 1:
            print("\nCantidad de millas: {}".format(viajero.cantidadTotaldeMillas()))
            system("pause")
        elif opc == 2:
            millas = int(input("\nIndique la cantidad de millas que acumuló: "))
            viajero.acumularMillas(millas)
            print("\nCantidad de millas actualizada: {}".format(viajero.cantidadTotaldeMillas()))
            system("pause")
        elif opc == 3:
            millas = int(input("\nIndique la cantidad de millas que desea canjear: "))
            viajero.canjearMillas(millas)
            system("pause")
        elif opc == 4:
            print('--** Gracias por utilizar nuestro sistema **--')
            break
        else:
            print("\n¡¡ERROR!! Opción Incorrecta")
            system("pause")
        system("cls")

if __name__ == "__main__":
    listaViajeros = ListaViajeros()
    listaViajeros.testListaViajeros()
    listaViajeros.mostrarViajeros()

    num = int(input("\nIndique un número de viajero: "))
    if listaViajeros.isNumViajero(num):
        menu()
    else:
        print("\n ¡¡ERROR!! El número de viajero indicado no existe")
