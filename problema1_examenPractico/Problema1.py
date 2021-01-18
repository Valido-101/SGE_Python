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



db = DB("ERP_FESAC")
'''
db.create("CREATE TABLE productos(id integer, nombre text PRIMARY KEY, preciocoste float, precioventa float, stockactual integer)")
db.create("CREATE TABLE stock(cdgproducto text, almacen text, stock integer, FOREIGN KEY (cdgproducto) REFERENCES productos(nombre), PRIMARY KEY(cdgproducto,almacen))")
db.create("CREATE TABLE movimientos(id integer PRIMARY KEY, fecha text, cdgproducto text, almacen text, tipo text, cantidad integer, FOREIGN KEY (cdgproducto) REFERENCES productos(nombre))")

productos = open("productos.txt", "r")

for linea in productos:
    valores = linea.split(",")
    db.insert("productos", valores)

productos.close()

stock = open("stock.txt", "r")

for linea in stock:
    valores = linea.split(",")
    db.insert("stock", valores)

stock.close()

movimientos = open("movimientos.txt", "r")

for linea in movimientos:
    valores = linea.split(",")
    db.insert("movimientos", valores)

stock.close()
'''

cantidad_vendida = db.select("SELECT SUM(cantidad) FROM movimientos WHERE cdgproducto='tornillo128' AND tipo='venta'")

print("Cantidad de 'tornillo128' vendidos:",cantidad_vendida)

db.__del__()

