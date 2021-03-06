'''
Created on 18-dic-2020

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