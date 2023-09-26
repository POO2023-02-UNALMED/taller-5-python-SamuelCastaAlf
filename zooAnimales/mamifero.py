from gestion import zona
from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        cab = Mamifero(nombre,edad,"pradera",genero,True,4)
        cls.caballos = cls.caballos+1
        return cab
    
    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        leo = Mamifero(nombre,edad,"selva",genero,True,4)
        cls.leones = cls.leones+1
        return leo
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls,mamifero):
        cls._listado.append(mamifero)

    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self,pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas
    
    def setPatas(self,patas):
        self._patas = patas