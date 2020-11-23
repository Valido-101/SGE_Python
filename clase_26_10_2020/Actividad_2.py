'''
Created on 26-oct-2020

@author: maxus
'''
nombre=input("Introduce tu nombre: ")
edad=input("Introduce tu edad: ")
altura=input("Introduce tu altura: ")
grupo_sanguineo=input("Introduce tu grupo sanguineo (A, B, 0): ")

leve=0
moderado=0
grave=0

if int(edad)<20 :
    leve+=60
    moderado+=30
    grave+=10
    
elif int(edad)>=20 & int(edad)<40:
    leve+=15
    moderado+=40
    grave+=45

elif int(edad)>=40 & int(edad)<50:
    leve+=30
    moderado+=40
    grave+=30

else:
    leve+=50
    moderado+=30
    grave+=20
    
if grupo_sanguineo=="A" and float(altura)<1.80:
        leve-=5
        moderado-=5
        grave-=5
        
elif grupo_sanguineo=="A" and float(altura)>1.80:
        leve+=10
        moderado+=10
        grave+=10
        
elif grupo_sanguineo=="B" and float(altura)<1.80:
        leve+=20
        moderado+=20
        grave+=20   
    
elif grupo_sanguineo=="0" and float(altura)>1.80:
        leve+=5
        moderado+=5
        grave+=5
    
print("Para el usuario ",nombre,":")
print("La probabilidad de contraer el virus F de forma leve es del: ",leve,"%")
print("La probabilidad de contraer el virus F de forma moderada es del: ",moderado,"%")
print("La probabilidad de contraer el virus F de forma grave es del: ",grave,"%")