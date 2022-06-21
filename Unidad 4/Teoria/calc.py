#HACER UNA CALCULADORA AUTOMATICA-

numero1= int(input("Ingrese el primer numero"))
numero2 = int(input("Ingrese el segundo numero"))

operacion = input("Que operacion ('+','-','*','/')?")

if (operacion == "+"):
    print(numero1 + numero2)
elif (operacion == "-"):
    print(numero1 - numero2)

#así separado o usando elif es lo mismo

import sys
print(sys.argv)

lista = sys.argv

numero1 = lista[1] #pq en la 0 es el nombre del programa
numero2 = lista[2]
operacion = lista[3]


# python calc.py 9 3 + (elemento 1 y 2 son los numeros y el 3 es la operacion, eso hay q escribirlo en la terminal)
#cd--> para cambiar directorio (carpeta). cd solo nos lleva a nuestro user, la "home" (c:\Users\florm)
'''
cd.., los puntos son para moverme un nivel más arriba, C:\Users\florm\PycharmProjects\pythonProject4 --> cd.. =
C:\Users\florm\PycharmProjects--> cd.. = 
C:\Users\florm, etc.
sube 1 carpeta (como q sale de la subcarpeta)
cd../.. --> te lleva a la raiz de una
para ir hasta una carpeta mas adelante--> python "que carpeta estan/Unidad 4/calc.py" ej desktop/Unidad4/calc.py
pwd para saber donde esta
Si quiero cambiar d unidad, hago 2 puntos "..", salgo d la unidad 3 por ej, y dsps entro a la unidad 4--> python ../unidad3/calc.py
o sino cd.. --> cd unidad4--> python calc.py (3 comandos)
'''