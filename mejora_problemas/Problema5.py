'''
Created on 30-nov-2020

@author: Usuario
'''
print("Programa de notas: ")

##Esto dara error porque se guardara como string y no se podra comparar con numeros
nota = input("Dime tu nota: ");

##Comprobamos primero si es numerico y si lo es lo guardamos como int si es menor o igual a diez
if nota.isnumeric() and int(nota)<=10:
    nota = int(nota)
    
    ##Controlamos los distintos casos con if-elif
    if nota >=0 and nota <5:
        print("Suspenso")

    elif nota >=5 and nota <6:
        print("Aprobado") 
    
    elif nota >=6 and nota <7:
        print("Bien")
    
    elif nota >=7 and nota <9:
        print("Notable") 
    
    elif nota >=9 and nota <10:
        print("Sobresaliente")
        
    elif nota == 10 :
        print("Honor") 
##Si no es numerica o es mayor a diez informamos de que la nota no es valida
elif nota.isnumeric()==False or int(nota)>10:
    print("Nota no valida")
