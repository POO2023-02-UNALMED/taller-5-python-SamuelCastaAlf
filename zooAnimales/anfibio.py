from gestion import zona
from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    def __init__(self,nombre,edad,habitat,genero,colorpiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._venenoso = venenoso
        self._colorPiel = colorpiel
        Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls,nombre,edad,genero):
        rana = Anfibio(nombre,edad,"selva",genero,"rojo",True)
        Anfibio.ranas = Anfibio.ranas+1
        return rana

    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        sala = Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        Anfibio.salamandras = Anfibio.salamandras+1
        return sala
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls,anf):
        cls._listado.append(anf)

    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self,colorpiel):
        self._colorPiel = colorpiel

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self,venenoso):
        self._venenoso = venenoso