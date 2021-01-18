'''
Created on 04-ene-2021

@author: Usuario
'''
from actividad3_db import db_class

db = db_class.DB("mi_erp")
'''
valores = tuple()

f = open("ventas.txt", "r")
for linea in f:
    valores=linea.split(",")
    db.insert("ventas", valores)
f.close()


for i in range(1,21):

    cadena = 'UPDATE ventas SET importe = (precio * cantidad) WHERE id = '+str(i)

    db.curs.execute(cadena)

db.con.commit()
'''

acum_ventas = open("Acum_ventas.csv", "w")

acum_ventas.write("Ciudad;Ventas\n")

ventas_data=db.select("SELECT ciudad,COUNT(ciudad) FROM ventas GROUP BY ciudad")

for i in ventas_data:
    acum_ventas.write(i[0]+";"+str(i[1])+"\n")

acum_ventas.close()

#----------------------------------------

acum_prod = open("Acum_productos.csv", "w")

acum_prod.write("Producto;Precio;Cantidad;Importe Total\n")

productos_data=db.select("SELECT codigo_producto_vendido,precio,SUM(cantidad),SUM(importe) FROM ventas GROUP BY codigo_producto_vendido")

for i in productos_data:
    acum_prod.write(str(i[0])+";"+str(i[1])+";"+str(i[2])+";"+str(i[3])+"\n")

acum_ventas.close()

db.__del__()