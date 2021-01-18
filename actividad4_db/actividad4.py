'''
Created on 21-dic-2020

@author: Usuario
'''
from actividad3_db import db_class

db = db_class.DB("prueba")
valores = tuple()

'''
f = open("empleados.txt", "r")
for linea in f:
    valores=linea.split(",")
    db.insert("empleados", valores)
f.close()
'''
programadores = open("Programadores.csv", "w")

programadores.write("nombre;salario anual;fecha contratacion;categoria\n")

data=db.select("SELECT nombre,salario,fecha_contratacion,categoria FROM empleados WHERE categoria='Programador'")

for i in data:
    programadores.write(i[0]+";"+str(i[1])+";"+i[2]+";"+i[3]+"\n")

programadores.close()

#-----------------------------------------------------

resumen = open("Resumen.csv", "w")

resumen.write("departamento;categoria;salariototal\n")

resumen_data=db.select("SELECT departamento,categoria,SUM(salario) FROM empleados GROUP BY categoria")

for i in resumen_data:
    resumen.write(i[0]+";"+i[1]+";"+str(i[2])+"\n")
    
resumen.close()

db.__del__()