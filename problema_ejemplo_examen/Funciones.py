'''
Created on 20-nov-2020

@author: maxus
'''
from problema_ejemplo_examen.Producto import Producto

def transformar_ventas(lista):
    list_dic = []
    for i_venta, producto, cantidad, ciudad, importe, nombre, precio, preciocoste in lista:
        d = {"cantidad":cantidad, "ciudad": ciudad, "importe": importe, "producto": Producto(nombre,precio,preciocoste)}
        list_dic.append(d)
    return list_dic

def calcular_importes(ventas):
    for v in ventas:
        v['importe'] = v['cantidad']*v['producto'].precio
    
def calcular_importes_totales(ventas):
    x=0;
    for v in ventas:
        x += v['cantidad']*v['producto'].precio
    return x