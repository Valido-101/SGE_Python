'''
Created on 30-nov-2020

@author: Usuario
'''
class producto:
    
    ##El atributo precio lo cambiaremos para que coincida con los parametros 
    ##del constructor y tenga sentido 
    def __init__ (self, nombre, stock, coste_produccion):
        self.__nombre= nombre
        self.__stock = stock
        self.__preciocoste = coste_produccion
    
    @property
    def nombre(self):
        return self.__nombre
     
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
     
    @property
    def stock(self):
        return self.__stock
     
    @stock.setter
    def stock(self,stock):
        self.__stock = stock
     
    @property
    def coste_produccion(self):
        return self.__coste_produccion
     
    @coste_produccion.setter
    def coste_produccion(self,coste_produccion):
        self.__coste_produccion = coste_produccion
   
        
def transformar_compras(lista):
        list_dic = []
        for i_venta, producto, cantidad, ciudad, importe, nombre, precio, preciocoste in lista:
        ##Aquí no se ha indentado correctamente
            d = {'cantidadtotal': cantidad, 'ciudad': ciudad, 'importe': importe, 'producto': producto(nombre, precio, preciocoste)}
            list_dic.append(d)
        return list_dic

def calcular_compras(compras):
    for v in compras:
        v['importe'] = v['cantidad']*v['producto'].precio

def cantidadtotal(cantidad):
    for v in cantidad:
        v['importe'] = v['cantidadtotal']*v['preciototal']
        
        
        
res = [(1,1,80,None,'producto1',1.5),
      (2,1,70,None,'producto1',1.5),
      (3,2,15,None,'producto2',1.8),
      (4,2,21,None,'producto2',1.8),
      (5,2,18,None,'producto2',1.8),
      (6,3,40,None,'producto3',2.1),
      (7,3,24,None,'producto3',2.1),
      (8,4,17,None,'producto4',2.4),
      (9,4,32,None,'producto4',2.4),
      (10,4,40,None,'producto4',2.4)]

coompras = transformar_compras(res)
##Compras no existe, se ha definido "coompras"
print(coompras)

##Este método no existe
ventas2 = calcular_compras(res)
##Compras no existe
print(ventas2)

ventas1 = transformar_compras(res)
calcular_compras(ventas1)
print(ventas1)