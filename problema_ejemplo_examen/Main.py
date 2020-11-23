'''
Created on 16-nov-2020

@author: maxus
'''
from problema_ejemplo_examen.Funciones import transformar_ventas,calcular_importes,calcular_importes_totales
    
Ventas=[(1,1,100,'Huelva',None,'producto1',15,9),
(2,1,100,'Sevilla',None,'producto1',15,9),
(3,2,100,'Sevilla',None,'producto2',18,11),
(4,2,100,'Sevilla',None,'producto2',18,11),
(5,2,100,'Huelva',None,'producto2',18,11),
(6,3,100,'Sevilla',None,'producto3',21,12),
(7,3,100,'Cordoba',None,'producto3',21,12),
(8,4,100,'Sevilla',None,'producto4',24,13),
(9,4,100,'Huelva',None,'producto4',24,13),
(10,4,100,'Cordoba',None,'producto4',24,13)]

diccionario = transformar_ventas(Ventas)
for d in diccionario:
    print(d)

print()

calcular_importes(diccionario)
for d in diccionario:
    print(d)
    
print()
    
print(calcular_importes_totales(diccionario))

