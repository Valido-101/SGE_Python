'''
Created on 30-oct-2020

@author: maxus
'''
s=(8,3,24,32,14,78,25,85,32,7,777,124)

x = int(input("Introduzca un numero: "))

contador=0

encontrar=False

for lista in s:
    if lista == x:
        encontrar=True
        contador+=1
if encontrar==True:
    print("Numero encontrado ",contador," veces.")
else:
    print("Numero no encontrado")
        