'''
Created on 20-nov-2020

@author: maxus
'''
class Producto:
    
    def __init__(self, nombre, precio, coste_produccion):
        self.__nombre=nombre
        self.__precio=precio
        self.__coste_produccion=coste_produccion
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, precio):
        self.__precio=precio
    @property
    def coste_produccion(self):
        return self.__coste_produccion
    @coste_produccion.setter
    def coste_produccion(self, coste_produccion):
        self.__coste_produccion=coste_produccion
    def toString(self):
        return self.__nombre,", ",self.__precio,", ",self.__coste_produccion