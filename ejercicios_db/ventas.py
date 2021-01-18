'''
Created on 14-dic-2020

@author: Usuario
'''
import sqlite3

try:
    con = sqlite3.connect("mi_erp.db")
    print("Conexion establecida a ","mi_erp.db")
except sqlite3.Error:
    print("No ha sido posible conectarse.")
  
cur = con.cursor()
'''
cur.execute("CREATE TABLE productos (id integer PRIMARY KEY, nombre text, precio_venta float, precio_coste float, stock_actual integer)")

cur.execute("CREATE TABLE stock (codigo_producto integer REFERENCES productos(id), almacen text, stock integer, PRIMARY KEY (codigo_producto, almacen))")

cur.execute("CREATE TABLE ventas (id integer PRIMARY KEY, codigo_producto_vendido integer REFERENCES productos(id), cantidad integer, ciudad text, importe float, precio float)")

con.commit()

#----------------------------------------------------

cur.execute("INSERT INTO productos(id) values(1)")
cur.execute("INSERT INTO productos(id) values(2)")
cur.execute("INSERT INTO productos(id) values(3)")
cur.execute("INSERT INTO productos(id) values(4)")
cur.execute("INSERT INTO productos(id) values(5)")
cur.execute("INSERT INTO productos(id) values(6)")
cur.execute("INSERT INTO productos(id) values(7)")
cur.execute("INSERT INTO productos(id) values(8)")
cur.execute("INSERT INTO productos(id) values(9)")
cur.execute("INSERT INTO productos(id) values(10)")

con.commit()

#-----------------------------------------------------

cur.execute("INSERT INTO ventas VALUES(1,1,100,'Huelva',null,15)")
cur.execute("INSERT INTO ventas VALUES(2,1,100,'Sevilla',null,15)")
cur.execute("INSERT INTO ventas VALUES(3,2,100,'Sevilla',null,18)")
cur.execute("INSERT INTO ventas VALUES(4,2,100,'Sevilla',null,18)")
cur.execute("INSERT INTO ventas VALUES(5,2,100,'Huelva',null,18)")
cur.execute("INSERT INTO ventas VALUES(6,3,100,'Sevilla',null,21)")
cur.execute("INSERT INTO ventas VALUES(7,3,100,'Cordoba',null,21)")
cur.execute("INSERT INTO ventas VALUES(8,4,100,'Sevilla',null,24)")
cur.execute("INSERT INTO ventas VALUES(9,4,100,'Huelva',null,24)")
cur.execute("INSERT INTO ventas VALUES(10,4,100,'Cordoba',null,24)")

con.commit()

for i in range(1,11):

    cadena = 'UPDATE ventas SET importe = (precio * cantidad) WHERE id = '+str(i)

    cur.execute(cadena)

con.commit()
'''

cur.execute("SELECT SUM(importe) FROM ventas GROUP BY ciudad HAVING ciudad='Huelva'")

print("Importes totales de Huelva: ",cur.fetchall())

cur.execute("SELECT SUM(importe) FROM ventas GROUP BY ciudad HAVING ciudad='Sevilla'")

print("Importes totales de Sevilla: ",cur.fetchall())

