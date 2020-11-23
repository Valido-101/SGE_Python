'''
Created on 13-nov-2020

@author: maxus
'''
class Edificacion:
    def __init__ (self, altura, constructora, valor_suelo, ubicacion):
        self.__altura=altura
        self.__constructora=constructora
        self.__valor_suelo=valor_suelo
        self.ubicacion=ubicacion
    
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura):
        self.__altura=altura
    
    @property
    def constructora(self):
        return self.__constructora
    @constructora.setter
    def constructora(self, constructora):
        self.__constructora=constructora
    
    @property
    def valor_suelo(self):
        return self.__valor_suelo
    @valor_suelo.setter
    def valor_suelo(self, valor_suelo):
        self.__valor_suelo=valor_suelo
    
    @property
    def ubicacion(self):
        return self.__ubicacion
    @ubicacion.setter
    def ubicacion(self, ubicacion):
        self.__ubicacion=ubicacion
    
    def descripcion(self):
        cadena="Altura: "+str(self.altura)+", Constructora: "+self.constructora+", Valor del suelo: "+str(self.valor_suelo)+", Ubicacion: "+self.ubicacion
        return cadena