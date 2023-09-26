from gestion import zona
from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self,nombre,edad,habitat, genero,colorescamas,cantidadaletas):
        super().__init__(nombre,edad,habitat,genero) 
        self._colorEscamas = colorescamas
        self._cantidadAletas = cantidadaletas
        Pez._listado.append(self)
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        sal = Pez(nombre,edad,"oceano",genero,"rojo",6)
        cls.salmones = cls.salmones+1
        return sal
    
    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        bac = Pez(nombre,edad,"oceano",genero,"gris",6)
        cls.bacalaos = cls.bacalaos+1
        return bac
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls,pez):
        cls._listado.append(pez)
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self,colorescamas):
        self._colorEscamas = colorescamas

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self,cantidadaletas):
        self._cantidadAletas = cantidadaletas