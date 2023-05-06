import datetime

class Registro:
    __diaMes: int
    __hora: int
    __temperatura: float
    __humedad: float   
    __presion: float
    def __init__(self, dia=0,hora=0, temperatura=None, humedad=None,presion= None):
        self.__diaMes=dia 
        self.__hora=hora
        self.__temperatura=temperatura
        self.__humedad=humedad
        self.__presion=presion
    def getDiaMes(self):
        return self.__diaMes
    def getHora(self):
        return self.__hora
    def getTemperatura(self):
        return self.__temperatura
    def getHumedad(self):
        return self.__humedad
    def getPresion(self):
        return self.__presion
  

    