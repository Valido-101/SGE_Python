'''
Created on 16-nov-2020

@author: maxus
'''
class Aula:
    def __init__(self, largo, ancho, alto, completamos=False):
        self.__largo=largo
        self.__ancho=ancho
        self.__alto=alto
        self.__aforo_completo=completamos
    
    def completo(self):
        if(self.__aforo_completo==True):
            print("Esta completo el aforo de la clase")
        else:
            print("No esta completo el aforo")
    
    def estado(self):
        cadena="Largo: "+str(self.__largo)+", Ancho: "+str(self.__ancho)+", Alto: "+str(self.__alto)+", Aforo completo: "+str(self.__aforo_completo)
        print(cadena)
    @property
    def largo(self):
        return self.__largo   
    
miaula = Aula(3,4,3)
miaula.completo()
print("El largo de mi clase es "+str(miaula.largo)+" metros.")
miaula.estado()
aula2 = Aula(3,4,3,True)
aula2.completo()
aula2.estado()