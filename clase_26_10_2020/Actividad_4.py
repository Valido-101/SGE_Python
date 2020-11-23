'''
Created on 30-oct-2020

@author: maxus
'''
s=(8,3,24,32,14,78,25,85,32,7,777,124)

def numMayor(s):
    
    mayor=s[0]
    
    for num in s:
        if num>mayor:
            mayor=num
    return mayor

def numMenor(s):
    
    menor=s[0]
    
    for num in s:
        if num<menor:
            menor=num
    return menor

mayor=numMayor(s)
menor=numMenor(s)

print("El numero mayor es ",mayor,", el numero menor es ",menor,". La distancia entre ambos es ",mayor-menor,"kilometros.")