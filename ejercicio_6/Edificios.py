'''
Created on 13-nov-2020

@author: maxus
'''
from ejercicio_6.Edificacion import Edificacion
from ejercicio_6.Piso import Piso

edificio2 = Edificacion(89,"San Jose",1800000,"Sevilla")
piso = Piso(73, "San Juan", 1890888, "Tomares", 500, 4, 2, 18000, 4, 1, "B")

print(edificio2.descripcion())
print(piso.descripcion_piso())