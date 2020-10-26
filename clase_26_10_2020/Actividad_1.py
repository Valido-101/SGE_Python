nombre=input("Introduce tu nombre: ")
edad=input("Introduce tu edad: ")
grupo_sanguineo=input("Introduce tu grupo sanguineo (A, B, 0): ")

poco_arriesgado=0
medio_arriesgado=0
muy_arriesgado=0

if int(edad)<20 :
    poco_arriesgado+=10
    medio_arriesgado+=30
    muy_arriesgado+=60
    
    if grupo_sanguineo=="A":
        poco_arriesgado-=5
        medio_arriesgado-=5
        muy_arriesgado-=5
        
    elif grupo_sanguineo=="B":
        poco_arriesgado+=20
        medio_arriesgado+=20
        muy_arriesgado+=20   
    
elif int(edad)>=20 & int(edad)<40:
    poco_arriesgado+=20
    medio_arriesgado+=40
    muy_arriesgado+=40
    
    if grupo_sanguineo=="A":
        poco_arriesgado-=5
        medio_arriesgado-=5
        muy_arriesgado-=5
        
    elif grupo_sanguineo=="B":
        poco_arriesgado+=20
        medio_arriesgado+=20
        muy_arriesgado+=20   
    
elif int(edad)>=40 & int(edad)<50:
    poco_arriesgado+=30
    medio_arriesgado+=40
    muy_arriesgado+=30
    
    if grupo_sanguineo=="A":
        poco_arriesgado-=5
        medio_arriesgado-=5
        muy_arriesgado-=5
        
    elif grupo_sanguineo=="B":
        poco_arriesgado+=20
        medio_arriesgado+=20
        muy_arriesgado+=20   
    
else:
    poco_arriesgado+=50
    medio_arriesgado+=30
    muy_arriesgado+=20
    
    if grupo_sanguineo=="A":
        poco_arriesgado-=5
        medio_arriesgado-=5
        muy_arriesgado-=5
        
    elif grupo_sanguineo=="B":
        poco_arriesgado+=20
        medio_arriesgado+=20
        muy_arriesgado+=20   
    
print("Para el usuario ",nombre,":")
print("La probabilidad de ser un inversor poco arriesgado es del: ",poco_arriesgado,"%")
print("La probabilidad de ser un inversor moderadamente arriesgado es del: ",medio_arriesgado,"%")
print("La probabilidad de ser un inversor arriesgado es del: ",muy_arriesgado,"%")