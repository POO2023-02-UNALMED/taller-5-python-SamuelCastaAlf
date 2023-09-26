from gestion import zona
from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    aguilas = 0
    halcones = 0
    def __init__(self,nombre,edad,habitat,genero,colorplumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas = colorplumas
        Ave._listado.append(self)
    
    @classmethod
    def cantidadAves():
        return len(Ave._listado)
    
    def movimeinto(self):
        return "volar"
    
    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        hal = Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        Ave.halcones = Ave.halcones+1
        return hal 
    
    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        agui = Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
        Ave.aguilas = Ave.aguilas+1
        return agui
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls,ave):
        cls._listado.append(ave)

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self,colorplumas):
        self._colorPlumas = colorplumas