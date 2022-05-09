class registro:
    __temperatura = 0.0
    __humedad = 0.0
    __presion = 0.0

    def __init__(self, temperatura, humedad, presion):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion

    def getTemperatura(self):
        return (self.__temperatura)

    def getHumedad(self):
        return int(self.__humedad)

    def getPresion(self):
        return int(self.__presion)
