'''
Created on 16-nov-2020

@author: maxus
'''
#Crea una clase hija llamada piso que tenga como propiedades iniciales 
#protegidas los metros_construidos, numero_habitaciones,numero_baños, precio, planta, 
#numero_piso y puerta. Los valores de estas propiedades deben ser definidas por un constructor
# y protegidas para que sólo puedan ser modificadas dentro de la clase. Además debe definir 
#un método denominado descripción_piso que da el valor de la todas las propiedades. 
#Cree un piso con las propiedades que considere oportunas
from ejercicio_6.Edificacion import Edificacion

class Piso(Edificacion):
    def __init__(self,altura, constructora, valor_suelo, ubicacion, metros_construidos, numero_habitaciones, numero_banios, precio, planta, numero_piso, puerta):
        Edificacion.__init__(self, altura, constructora, valor_suelo, ubicacion)
        
        self.__metros_construidos=metros_construidos
        self.__numero_habitaciones=numero_habitaciones
        self.__numero_banios=numero_banios
        self.__precio=precio
        self.__planta=planta
        self.__numero_piso=numero_piso
        self.__puerta=puerta
        
    @property
    def metros_construidos(self):
        return self.__metros_construidos
    
    @metros_construidos.setter
    def metros_construidos(self,metros_construidos):
        self.__metros_construidos=metros_construidos
        
    @property
    def numero_habitaciones(self):
        return self.__numero_habitaciones
    
    @numero_habitaciones.setter
    def numero_habitaciones(self,numero_habitaciones):
        self.__numero_habitaciones=numero_habitaciones
        
    @property
    def numero_banios(self):
        return self.__numero_banios
    
    @numero_banios.setter
    def numero_banios(self,numero_banios):
        self.__numero_banios=numero_banios
        
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,precio):
        self.__precio=precio
        
    @property
    def planta(self):
        return self.__planta
    
    @planta.setter
    def planta(self,planta):
        self.__planta=planta
        
    @property
    def numero_piso(self):
        return self.__numero_piso
    
    @numero_piso.setter
    def numero_piso(self,numero_piso):
        self.__numero_piso=numero_piso
        
    @property
    def puerta(self):
        return self.__puerta
    
    @puerta.setter
    def puerta(self,puerta):
        self.__puerta=puerta
        
    def descripcion_piso(self):
        cadena=self.descripcion()+", Metros construidos: "+str(self.metros_construidos)+", Numero de habitaciones: "+str(self.numero_habitaciones)+", Numero de bannios: "+str(self.numero_banios)+", Precio: "+str(self.precio)+", Planta: "+str(self.planta)+", Numero de piso: "+str(self.numero_piso)+", Puerta: "+self.puerta
        return cadena