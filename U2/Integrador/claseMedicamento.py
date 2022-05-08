class Medicamento:
    __idCama: int
    __idMedicamento: int
    __nombreComercial: str
    __monodroga: str
    __presentacion: str
    __cantidadAplicada: int
    __precioTotal: float

    def __init__(self, cama=0, medicamento=0, nombre=None, monodroga=None, presentacion=None, cantidad=0, precio=0):
        self.__idCama = cama
        self.__idMedicamento = medicamento
        self.__nombreComercial = nombre
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cantidadAplicada = cantidad
        self.__precioTotal = precio

    def getIdCama2(self):
        return self.__idCama

    def getIdMedicamento(self):
        return self.__idMedicamento

    def getNombreComercial(self):
        return self.__nombreComercial

    def getMonodroga(self):
        return self.__monodroga

    def getPresentacion(self):
        return self.__presentacion

    def getCantidadAplicada(self):
        return self.__cantidadAplicada

    def getPrecioTotal(self):
        return self.__precioTotal
