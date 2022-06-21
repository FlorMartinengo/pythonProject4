""" Un diccionario es un diccionario pq tiene clave y valor. Conjunto de clave valor
Se pueden representar muchas cosas. Nombre(clave): Rodrigo(valor), Apellido: Sellanes. Estructura de dato esencial
Un diccionario puede tener infinitos conjuntos de clave valor.
Se definen con lLaves y  dos puntos"""

print("\n")

cliente = { "nombre": "mark", "dni": "44669617"}
print(cliente["nombre"].title())

"""Metodos:
keys()
values()
items()
get()
todos devuelven una lista"""

login = {"username": "florencia",
         "password": "flor123"} #definimos un diccionario con 2 claves

valores = login.values() #te devuelve los valores en una lista
print(valores)

#ciclo, iteracion, loop, es todo lo mismo

items = login.keys() #tmb te devuelve una lista pero de las claves
print(items)

"""Funciones:
del()
set()
sorted()
len()"""

print("\n-----Ejercicio 1-----")
#Ejercicio 1- Usuario de ventas
"""Crear un programa y utilizando lo visto de diccionarios guardar la información 
de un usuario de un sistema de Administración de Ventas. 
Los datos que guardaremos son:
nombre, apellido, dni, rol, sucursal --> CLAVES
Luego mostrar el resultado por consola/pantalla.
Luego mostrar cada una de los valores en un print separado."""

print("\n")

usuario = {"nombre":"","apellido":"","dni":"","rol":"","sucursal":""}
print(usuario) #te lo devuelve como está, los valores de string vacios

print("\n")

usuario2 = {"nombre":"Martin","apellido":"Odersky","dni":"1239123","rol":"CFO","sucursal":"001"}
print(usuario2)

#001 en string, si lo pondriamos como número no devuelve los 0, solo 1 devolveria.

print("\n")

print(usuario2.values()) #devuelve cada uno de los valores.
#Nosotros no queremos que devuevlva "dict_values(): "

print("\n")

for data in usuario2.values():
    print(data)
        #for se itera hasta q termina la lista

print("\n")

for data in usuario2.keys():
    print(data) #acá estan en minusculas

print("\n")

for data in usuario2.keys():
    print(data.title()) #acá mayúsculas

print("\n")

print(usuario2.items()) #devuelve tuplas con cada clave y valor

print("\n")

for data in usuario2.items():
    print(data)

print("\n")

for key, value in usuario2.items():
    print(key, value) #le decimos a for q el elemento key lo guarde en key y value en value
#imprime la clave y valor. podriamos haber printeado solo las key y da las key
#el ej ya está falta darle "styling"

print("\n")

for key, value in usuario2.items():
    print(key.title())
    print(value) #asi imprime en una fila distinta

print("\n")

for key, value in usuario2.items():
    print("{key.title()}:{value}")
    """f, esta en la guia 2. si al string lo queremos hacer dinamico tenemos
    que poder pasarle valores. Con la f podemos utilizar variables dentro de un string
    si no ponemos la f lo muestra como un string plano"""

print("\n")

for key, value in usuario2.items():
    print(f"{key.title()}: {value}")

print("\n")

#Queremos q DNI esté todo en mayúsculas:
for key, value in usuario2.items():
    if key == "dni":
        print(f"{key.upper()}: {value}")
    else:
        print(f"{key.title()}: {value}")

print("\n")

# ó sino al revés
for key, value in usuario2.items():
    if key != "dni":
        print(f"{key.title()}: {value}")
    else:
        print(f"{key.upper()}: {value}")

print("\n-----Ejercicio 2-----")
#Ejercicio 2

"""Queremos comprender específicamente la diferencia de las estructuras de datos que hemos
visto hasta el momento. Las cuales son:
● Lista “[]”
● Tupla “()”
● Conjunto “{}”
● Diccionario “{k:v}”
Desarrollar un programa y dentro definir una variable “animals_<type>” para cada tipo
de estructura de datos. A todas las estructuras les vamos a asignar 3 animales por defecto,
los que más gusten. Luego vamos a realizar las siguientes pruebas:
● Utilizando la función “print()” imprimir cada una de ellas. Debatir el output en
cada caso.
● Agregar a la función “print()” “type(animals_<type>)” al final.
● Utilizando los métodos correctos para cada caso, intentar agregar un nuevo animal
“python” a cada estructura. ¿Qué sucede en cada caso?
Ing. Rodrigo Sellanes
● Finalmente a la estructura “conjunto” intentar agregar nuevamente “python”. ¿Qué
resultado obtenemos?"""

#conjuntos = sets, tuplas = tuples, diccionarios = mapas

animals_list = ["cat", "elephant", "bird"]
animals_tuple = ("cat", "elephant", "bird") #no pueden modificarse
animals_set = {"cat", "elephant", "bird"}
animals_dict = {"cat": "cat", "elephant": "elephant", "bird": "bird"} #diccionario no es lo más óptimo

print(animals_list)
print(animals_tuple)
print(animals_set)
print(animals_dict)

print("\n")

print(f"{animals_list} - {type(animals_list)}")
print(f"{animals_tuple} - {type(animals_tuple)}")
print(f"{animals_set} - {type(animals_set)}")
print(f"{animals_dict} - {type(animals_dict)}")

print("\n")
#agregamos un nuevo animal "phyton"

python_animal = "phyton"
animals_list.append(python_animal) #lo agrega al final de la lista
print(animals_list)

print("\n")

"""animals_tupple.append(python_animal) #no existe el metodo append para esta estructura de datos
print(animals_tuple) #los unicos metodos disponibles--> count() e index().
# las podemos cambiar arriba, cuando la hacemos, pero dsps no se puede modificar"""

animals_set.add(python_animal) #set no tiene append, tiene add. Esto se puede ver en w3schools
print(f"Set elements: {animals_set}")#https://www.w3schools.com/python/python_ref_set.asp

#set: lista d elementos desordenados, la adición de phyton la puso en el medio, no al final

animals_set.add(python_animal)
animals_set.add(python_animal)
animals_set.add(python_animal)
print(f"Set elements: {animals_set}")
#aunque lo agreguemos muchas veces se agrega solo 1, set no acepta datos duplicados

#Ej 3 ya lo hicimos arriba- DNI mayus
print("\n-----Ejercicio 4-----")
#Ejercicio 4

"""Nos encontramos trabajando en una corporación multinacional. El área de People (recursos
humanos) está realizando una encuesta para ver de agregar a los beneficios de empleados
un boucher mensual en alimentos sustentables. Como la encuesta es anónima solo
tendremos a nuestra disposición los valores de cada persona.
En envían una diccionario de datos donde la key es “anonimoX” y el valor es de una escala
de “1 - 10”. Aquellas personas que no contestaron la encuesta quedan marcadas como “x”.

{'anonimo1': '6', 'anonimo2': '9', 'anonimo3': '5', 'anonimo4':
'x', 'anonimo5': 'x', 'anonimo6': '8', 'anonimo7': '3',
'anonimo8': '10', 'anonimo9': '4', 'anonimo10': '5', 'anonimo11':
'x', 'anonimo12': '2', 'anonimo13': '7', 'anonimo14': '5',
'anonimo15': '2', 'anonimo16': '8', 'anonimo17': '10'}

Desarrollar un programa que cumpla las siguientes características:
● Contar cuántos empleados no contestaron la encuesta y eliminarlos del diccionario.
Mostrar la cantidad por consola/pantalla.
● Generar un nuevo diccionario y guardar dentro todos los encuestados que sí
respondieron. Mostrar la cantidad por consola/pantalla.
● Sumar todos los valores de las encuestas y calcular el porcentaje de aceptación de
la propuesta que realizó el área de People.
● Finalmente obtener un listado de los números con los que valoraron la propuesta.
Los mismos no deben estar repetidos. Utilizar la función “sorted()” para ordenarlos"""

polling_original = {'anonimo1': '6', 'anonimo2': '9', 'anonimo3': '5', 'anonimo4':
'x', 'anonimo5': 'x', 'anonimo6': '8', 'anonimo7': '3',
'anonimo8': '10', 'anonimo9': '4', 'anonimo10': '5', 'anonimo11':
'x', 'anonimo12': '2', 'anonimo13': '7', 'anonimo14': '5',
'anonimo15': '2', 'anonimo16': '8', 'anonimo17': '10'}

#tenemos un diccionario con muchas clave valor (17), en el cual la clave es "anonimo".
#como las claves son unicas, no pueden repetirse, son anonimo1,2,3,etc.
#podría haber sido una lista ["6","9","5","x","x","8", etc]

#empleados q no contestaron la encuesta = x:
#en diccionario puedo usar 2 variables en el for

#1) empleados q con contestaron la encuesta = x    14:30hs
not_reply = 0

for poll, value in polling_original.items():
    if value == "x":
        not_reply += 1
print(f"Empleados que no contestaron: {not_reply}")

#2) diccionario con encuestados q si respondieron
#generar un nuevo diccionario

replied = {}
for poll, value in polling_original.items():
    if value != "x":
        replied[poll] = value

#poll y value se pueden repetir pq son variables temporales
#para agregar al diccionario se usa eso d ahi arriba... 14:40mins

print(f"Empleados que contestaron: {replied}")

print("\n")

#3) Sumar los valores...
print(len(replied))
#nos dice la cantidad de clave-valores q tiene, nosotros tenemos q obtener la suma d los valores

reply_sum = 0 #el define todas las variables arriba, en el head del archivo.

for value in replied.values():
    reply_sum += int(value)
print(reply_sum)

"""values() pq no nos interesan las claves, solo los valores.
 da una lista d valores
 lo paso a numero, sino da error"""

print("\n")

max_acceptance = 10 #es el maximo, escala del 1 al 10, en el enunciado lo dice
#definimos la variable para no dejar el numero suelto y no saber q es dsps

print(f"Total de encuestas contestadas: {len(replied)}")
print(f"Suma total de aceptación: {reply_sum}")
print(f"Porcentaje de aceptación: {(reply_sum * 100) / (max_acceptance * len(replied))}")

""" Constantes != Variables. not_reply, reply_sum, variables. cambian
max_acceptance constante, se mantiene siempre igual"""

print("\n")
#4) TAREA
#Sorted()--> investigar

# EJERCICIO 6 TAREA