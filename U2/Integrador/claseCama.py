from datetime import datetime


class Cama:
    __idCama: int
    __habitacion: int
    __estado: bool
    __apellidoNombre: str
    __diagnostico: str
    __fechaInternacion: str
    __fechaAlta: str

    def __init__(self, habit=0, ocupa=False, apell_nombr=None, diagn=None, internacion=None, alta=None):
        self.__idCama = 0
        self.__habitacion = habit
        self.__estado = ocupa
        self.__apellidoNombre = apell_nombr
        self.__diagnostico = diagn
        self.__fechaInternacion = internacion
        self.__fechaAlta = alta

    def getHabitacion(self):
        return self.__habitacion

    def getEstado(self):
        return self.__estado

    def getNombreyApellido(self):
        return self.__apellidoNombre

    def getDiagnostico(self):
        return self.__diagnostico

    def getFechInternacion(self):
        return self.__fechaInternacion

    def ModificarFechAlta(self):
        self.__fechaAlta = str(datetime.today())

    def getFechAlta(self):
        return self.__fechaAlta
