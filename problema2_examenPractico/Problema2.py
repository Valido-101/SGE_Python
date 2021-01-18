'''
Created on 18-ene-2021

@author: Usuario
'''
import sqlite3
from sqlite3 import Error
class DB:
    def __init__(self,nombre_fichero=":memory:"):   
        try:
                self.con = sqlite3.connect(nombre_fichero+".db")
                print("Conexion establecida a ",nombre_fichero)
                self.curs=self.con.cursor()
        except Error:
                print("No ha sido posible conectarse.")
                self.con = None
        
    def create(self,sql):
        try:
            self.curs.execute(sql)
            self.con.commit()
            print("Sentencia ejecutada con exito")
    
        except sqlite3.OperationalError:
            print("La tabla ya existe")
    
    def insert(self,nombre_tabla,valores):
        values=""
        for i in range(len(valores)):
            if(i==len(valores)-1):
                values=values+valores[i]
            else:
                values=values+valores[i]+","
        self.curs.execute("INSERT INTO "+nombre_tabla+" VALUES("+values+")")
        self.con.commit()
        
    def select(self,sql):
        self.curs.execute(sql)
        data=self.curs.fetchall()
        return data
    
    def __del__(self):
        self.curs.close()
        
db = DB("bd_compras")
'''
db.create("CREATE TABLE compras(id integer PRIMARY KEY, fecha text, cdgproducto text, proveedor integer, cantidad integer, precio float, importecompra float)")

compras = open("compras.txt","r")

for linea in compras:
    valores = linea.split(",")
    db.insert("compras", valores)

for i in range(1,101):

    cadena = 'UPDATE compras SET importecompra = (precio * cantidad) WHERE id = '+str(i)

    db.curs.execute(cadena)
    
db.con.commit()
'''

#------------------------------------------------------------------------------------------

compras_proveedor = open("Compras_Proveedor.csv","w+")

compras_proveedor.write("Proveedor;Acumulado de compras\n")

acum_compras = db.select("SELECT proveedor,SUM(cantidad) FROM compras GROUP BY proveedor")

for proveedor in acum_compras:
    compras_proveedor.write(str(proveedor[0])+";"+str(proveedor[1])+"\n")
    
compras_proveedor.close()
    
#-------------------------------------------------------------------------------------------

compras_productos = open("Compras_Productos.csv","w+")

compras_productos.write("Producto;Precio;Cantidad Total;Importe Total\n")

acum_productos = db.select("SELECT cdgproducto,precio,SUM(cantidad),SUM(importecompra) FROM compras GROUP BY cdgproducto")

for producto in acum_productos:
    compras_productos.write(str(producto[0])+";"+str(producto[1])+";"+str(producto[2])+";"+str(producto[3])+"\n")
    
compras_productos.close()