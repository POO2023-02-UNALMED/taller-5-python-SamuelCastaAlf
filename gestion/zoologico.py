import zooAnimales
from zooAnimales.animal import Animal
    
class Zoologico():
    def __init__(self,nombre,ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zona = []

    def agregarZonas(self,zona):
        self._zona.append(zona)

    def cantidadTotalAnimales(self):
        return Animal.getTotalAnimales()
    
    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self,ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._zona
    
    def setZona(self,zona):
        self._zona = zona