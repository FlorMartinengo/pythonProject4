
print("\n--- Clase 26-04 ---\n")

def sum_numbers(num1,num2):
    print(f"La suma es: {num1 + num2}")

sum_numbers(10,20)

print("\n")

def sum_numbers2(num1,num2):
    print(f"La suma es: {num1 + num2}")
    print(f"Num1: {num1}")
    print(f"Num2: {num2}")

sum_numbers2(10,20)

#Las funciones pueden retornar valores, listas, etc.

print("\n")

def sum_numbers3(num1,num2):
    print(f"La suma es: {num1 + num2}")
    print(f"Num1: {num1}")
    print(f"Num2: {num2}")
    return num1 + num2

sum = sum_numbers3(10,20)
print(sum)

print("\n")

list_numbers= [1,2,3,4]

def print_list(list):
    for element in list:
        print(element)

print(print_list(list_numbers))


print("\n")

list_numbers = [1, 2, 3, 4]

def modify_list(list):
    for element in list:
        element += 1
    return list

print(modify_list(list_numbers))
#no funciona, a el tmp.

print("\n")

list_numbers = [1, 2, 3, 4]

def modify_list2(list):
    list.append(5)

modify_list2(list_numbers[:]) #copia la lista para no modificar la original
print(list_numbers) #medio raro no funciona nd xd

# EJERCICIO WARMING UP
print("\n ----- WARMING UP, U5 ----- \n")

""" Comencemos por definir una función que reciba el nombre de una/un deportista profesional 
y el deporte que practica, luego lo guarde en una lista llamada “sportsmen”.
Finalmente crear otra función que reciba como parámetros la lista de textos, itere cada uno
de los elementos mostrando por consola/pantalla el siguiente texto “El/La deportista
{sportsman}, juega {sport}”. Debatir sobre: la definición de una función, las variables locales,
globales. Modificación de una lista y por último la llamada de una función."""

"""

sportsman = []

def save_sportman(sportsman, sport):
    sportsman_dict = {}
    sportsman_dict["Sportsman"] = sportsman
    sportsman_dict["Sport"] = sport

def print_sportsman(lista_deportistas):
    for deportista_dict in lista_deportistas: #para iterar lista usamos for
        print(f"El/la deportsta {deportista_dict('Sportsman')}, juega {deportista_dict('sport')}")

while True:
    print("(1) Agregar deportista")
    print("(2) Ver listado de deportistas")

    option = input(">> ")

    if option == "1":
        print("Nombre del deportista:")
        sportsman = input(">> ")
        print("Deporte que practica:")
        sport = input(">> ")

        save_sportman(sportsman,sport)

    if option == "2":
        print_sportsman(sportsman)
        
 """

#copypesteado de lo de el: (el mio no funciona)

sportsmen = []

def save_sportsmen(sportsman, sport):
    sportsman_dict = {}
    sportsman_dict['sportsman'] = sportsman
    sportsman_dict['sport'] = sport

    sportsmen.append(sportsman_dict)

def print_sportsmen(lista_deportistas):
    for deportista_dict in lista_deportistas:
        print(f"El/La deportista {deportista_dict['sportsman']}, juega {deportista_dict['sport']}")

while True:
    print("(1) Agregar deportista")
    print("(2) Ver listado de deportistas")

    option = input(">> ")

    if option == "1":
        print("Nombre del deportista")
        sportsman = input(">> ")
        print("Deporte que practica")
        sport = input(">> ")

        save_sportsmen(sportsman, sport)

    if option == "2":
        print_sportsmen(sportsmen)

    if option == "quit":
        break

# EJERCICIO 1
print("\n ----- EJERCICIO 1, U5 ----- \n")

""" Sigamos poniendo a prueba nuestras habilidades con funciones. Otro ejercicio del estilo
warming up. Desarrollar en clase, solo los alumnos.
Sabemos que un carrito de e-commerce no es algo fácil de programar, pero en esta ocasión
vamos a realizar una simulación acortando el scope. Desarrollar un programa que cumpla
las siguientes características.
● Definir una lista vacía llamada “shopping_cart”
● Los productos que agregamos al carrito deben ser ingresados por consola utilizando
la función vista anteriormente, “input()”.
● Guardar los productos, (nombre del producto y cantidad) en la lista.
● Tener una opción “comprar” la cual instancie una función “buy_shopping_cart”
mostrando la lista de productos dentro del carrito."""


#hecho por el: esta en el word
