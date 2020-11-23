'''
Created on 09-nov-2020

@author: maxus
'''
texto ="En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivia"
texto+=" un hidalgo de los de lanza en astillero adarga antigua rocin flaco y galgo corredor Una olla de"
texto+=" algo mas vaca que carnero salpicon las mas noches duelos y quebrantos los sabados"
texto+=" lantejas los viernes algun palomino de anadidura los domingos consumian las tres partes de"
texto+=" su hacienda El resto della concluian sayo de velarte calzas de velludo para las fiestas con"
texto+=" sus pantuflos de lo mesmo y los dias de entresemana se honraba con su velloi de lo mas fino"
texto+=" Tenia en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los"
texto+=" veinte y un mozo de campo y plaza que asi ensillaba el rocin como tomaba la podadera"
texto+=" Frisaba la edad de nuestro hidalgo con los cincuenta anos Era de complexion recia seco de"
texto+=" carnes enjuto de rostro gran madrugador y amigo de la caza Quieren decir que tenia el"
texto+=" sobrenombre de Quijada o Quesada que en esto hay alguna diferencia en los autores que"
texto+=" deste caso escriben aunque por conjeturas verisimiles se deja entender que se llamaba"
texto+=" Quijana Pero esto importa poco a nuestro cuento basta que en la narracion del no se salga un"
texto+=" punto de la verdad"

palabras = texto.split()

diccionario = dict()

palabra_buscada = input("Introduzca la palabra que quiera buscar: ")

for x in palabras:
    if(x==palabra_buscada):
        diccionario[x]=palabras.count(x)
if(diccionario.__len__()<1):
    print("Esta palabra no esta en el texto")
else:
    print(diccionario)