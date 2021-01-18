'''
Created on 14-dic-2020

@author: Usuario
'''
import sqlite3
from sqlite3 import Error

def crear_Bd(nombre_bd):
    try:
        con = sqlite3.connect(nombre_bd)
        print("Conexion establecida a ",nombre_bd)
    except Error:
        print("No ha sido posible conectarse.")
        con = None
    finally:
        return con
    
con = crear_Bd("prueba.db")

curs = con.cursor()
'''
try:
    curs.execute("CREATE TABLE empleados(id integer PRIMARY KEY, nombre text, salario float, departamento text, categoria text, fecha_contratacion text)")
    
    con.commit()
    
    print("Tabla creada con exito")
    
except sqlite3.OperationalError:
    print("La tabla ya existe")


try:
    curs.execute("INSERT INTO empleados VALUES(1,'Josepe',2100.3,'D1','Analista','01-07-2015')")
    curs.execute("INSERT INTO empleados VALUES(2,'Joseju',2100.3,'D1','Programador','01-07-2015')")
    curs.execute("INSERT INTO empleados VALUES(3,'Joselu',2100.3,'D1','Becario','01-07-2015')")
    
    con.commit()
    
    print("Empleados insertados correctamente")

except sqlite3.IntegrityError:
    print("Estos empleados ya existen")


try:
    curs.execute("INSERT INTO empleados VALUES(4,'Lolo',2100.3,'D1','Programador','15-03-2020')")
    curs.execute("INSERT INTO empleados VALUES(5,'Lilo',2100.3,'D1','Programador','15-03-2020')")
    curs.execute("INSERT INTO empleados VALUES(6,'Lulo',2100.3,'D1','Programador','15-03-2020')")
    curs.execute("INSERT INTO empleados VALUES(7,'Lalo',2100.3,'D1','Programador','15-03-2020')")
    curs.execute("INSERT INTO empleados VALUES(8,'Lelo',2100.3,'D1','Becario','15-03-2020')")
    
    con.commit()
    
    print("Empleados insertados correctamente")

except sqlite3.IntegrityError:
    print("Estos empleados ya existen")


curs.execute("UPDATE empleados SET categoria='Programador' WHERE categoria='Becario' AND fecha_contratacion='01-07-2015'")

con.commit()

print("Actualizacion realizada con exito")
'''

curs.execute("SELECT SUM(salario) FROM empleados WHERE categoria='Programador' OR categoria='Analista' GROUP BY categoria")

data = curs.fetchall()

print("Salario de los programadores: ",data[0],"Salario del analista: ",data[1])
