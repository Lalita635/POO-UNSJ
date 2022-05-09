class PlanAhorro:
    __codigo = int
    __modelo = ''
    __version = ''
    __precio = float
    __cuotas = int
    __licitar = int

    def __init__(self, c, mod, v, p, cta=0, lic=0):
        self.__codigo = c
        self.__modelo = mod
        self.__version = v
        self.__precio = p
        self.__cuotas = cta
        self.__licitar = lic

    def getCodigo(self):
        return self.__codigo

    def getModelo(self):
        return self.__modelo

    def getVersion(self):
        return self.__version

    def getPrecio(self):
        return self.__precio

    def modificaPrecio(self, p2):
        self.__precio = p2
        print('**-- Precio Modificado! --**\n')

    def mostrar(self):
        return print('Código: {}, Modelo: {}, Versión: {}'.format(self.__codigo, self.__modelo, self.__version))

    @classmethod
    def getLicitar(cls):
        return cls.__licitar

    @classmethod
    def getCuotas(cls):
        return cls.__cuotas

    @classmethod
    def modificaLicitar(cls, t):
        cls.__licitar = int(t)

    @classmethod
    def modificaCuotas(cls, w):
        cls.__cuotas = int(w)

    @classmethod
    def muestra(cls):
        print('\n Cantidad de cuotas: ' + str(cls.getCuotas()))
        print('\n Cuotas a licitar: ' + str(cls.getLicitar()))
