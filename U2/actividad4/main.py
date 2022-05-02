from claseVentana import Ventana


def test():
    print('Datos correctos:')
    pruebaok1 = Ventana('Prueba1', 450, 450, 3, 3)
    pruebaok1.mostrar()
    pruebaok2 = Ventana('Prueba1', 450, 450, 3, 3)
    pruebaok2.mostrar()
    print('Datos incorrectos: (coordenadas inferiores x < 0 )')
    pruebax0 = Ventana('Prueba1', 430, 430, -1, 7)
    print('Datos incorrectos: (coordenadas inferiores < 0 )')
    pruebay0 = Ventana('Prueba2', 400, 400, 5, -3)
    print('Datos incorrectos: (coordenada superior x > 500 )')
    pruebax600 = Ventana('Prueba3', 600, 490, 5, 5)
    print('Datos incorrectos: (coordenada superior y > 500 )')
    pruebax600 = Ventana('Prueba3', 300, 520, 4, 4)


if __name__ == '__main__':
    resp = input('Desea ejecutar el test?: 1.SI 2.NO')
    if resp == '1':
        test()
    else:
        print('Test no realizado')

    print('==== Ventana Inicio ====')
    ventanaInicio = Ventana('Inicio')
    ventanaInicio.mostrar()
    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(), ventanaInicio.alto(), ventanaInicio.ancho()))

    print('==== Ventana Cargar ====')
    ventanaCargar = Ventana('Cargar', 10, 20)
    ventanaCargar.mostrar()

    print('*** Mueve a la derecha ***')
    ventanaCargar.moverDerecha(10)
    ventanaCargar.mostrar()

    print('*** Mueve a la izquierda ***')
    ventanaCargar.moverIzquierda(10)
    ventanaCargar.mostrar()

    print('*** Bajar ***')
    ventanaCargar.bajar(10)
    ventanaCargar.mostrar()

    print('==== Ventana Borrar ====')
    ventanaBorrar = Ventana('Borrar', 10, 20, 100, 200)
    ventanaBorrar.mostrar()

    print('*** Subir ***')
    ventanaBorrar.subir(5)
    ventanaBorrar.mostrar()

    print('*** Subir ***')
    ventanaBorrar.subir()
    ventanaBorrar.mostrar()

    print('*** Bajar ***')
    ventanaBorrar.bajar()
    ventanaBorrar.mostrar()
