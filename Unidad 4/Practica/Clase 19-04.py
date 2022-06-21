#ciclo for, directiva for, statement (todo lo mismo)
""" for y while son interadores. generan ciclos, sube y baja. los ciclos
lo hacen sobre determinadas estructuras. ej:"""

vacaciones = "Brasil"
#tiene sentido que use for para vacaciones? no
print(len(vacaciones))

#for y while sirve para cuando tenemos q contar caracteres

#Ejercicio 6, Unidad 3--> lo habla desde las 13:08
""" tiene sentido tener un for dentro d un for? si."""

#Pasamos a la unidad 4
"""
Input-> funcion q permite a los usuarios ingresar dato, por linea de comando -la pantalla
negra de abajo-. El input frena al programa, lo pausa. Espera una entrada del usuario.
Una vez q escribimos continua el flujo, hasta q se encuentra con otro input. Input
recibe como parametro un string
"""
name = input("Please enter your name: ")
print(f"Hola {name}")
print("Fin del programa")

#hasta que no pongamos el nombre el programa queda pausado

print(type(name)) #es un string si ponemos nombre pero tmb string si escribo un numero

name = int(name)
print(type(name)) #ahora si es un int

"""
Hay 3 "diseños" para while
When to quit
Flag
Break
"""

# When to quit
message = ""
while message != "quit":
 message = input("Enter your name: ")
print(message)

#while ejecuta hasta q se cumpla, no termina. hasta que no escribimos quit
# no termina. el codigo queda dando vuelta en estas lineas


# Flag
active = True
while active:
 message = input("Enter your name: ")
 if message == "quit":
  active = False
 else:
  print(message)

"""definimos una banderita, flag, en este caso active. tiene q empezar en true, para 
que el programa siga ejecutandose. dsps le cambiamos d color a la bandera -false- para q frene
while true= no frenes nunca. active es true entonces es lo mismo q decir while true
si el mensaje es quit el programa termina pq al volver a comenzar el while es false"""

#Break
# es para salir del ciclo

while True:
 name = input("Enter your name: ")
 if name == "quit":
   break
print(name)

#que nunca deje de hacer el input -while-, pero.. if name es quit, cortar el ciclo de interacion


#ERRORES EN EJECUCION
try:
  print(10/0)
except ZeroDivisionError: #si llega a dar este error, imprimir lo d abajo. sino pondriamos esto salidra el traceback -lo rojo-
  print("No es posible dividir por 0")

"""
try:
  print(10/0)
except NameError: #en este caso no es un name error, asi q salta el error normal, sin texto
  print("No es posible dividir por 0")
"""

#Ejercicio 1:
"""
Las nuevas tendencias en autoservicio, tanto sea para compras de productos en
supermercados, recarga de créditos en diferentes tarjetas, etc. han impulsado al parque de
diversiones Disney World ubicado en Orlando, a 
desarrollar unos tótems donde los clientes ingresan su edad y el sistema les dice el monto a pagar. 
Es un programa bien simple pero tiene que contar con todas las condiciones que nos solicitan.

Debemos realizar un programa que le de la bienvenida a los clientes mostrando algún texto
decorado. Para ellos utilizar la función print() y con algo de creatividad, Disney valora
mucho este aspecto.

Seguido mostrar un mensaje “Buy a ticket, please enter your age” y habilitarle
un prompt al usuario para que pueda ingresar su edad.

● Si la edad del cliente es menor a 5, el ticket es free
● Si la edad del cliente es mayor e igual 5 y menor a 9, el ticket cuesta U$s 15
● Si la edad del cliente es mayor e igual 9 y menor a 14, el ticket cuesta U$s 23
● Si la edad del cliente es mayor e igual 14 y menor a 100, el ticket cuesta U$s 35
● Y finalmente si el cliente es mayor o igual a 100, mostrar el siguiente mensaje “Your
awesome!! Free ticket for you”

Tener presente que el programa debe permanecer vivo -while true-, para poder asistir a otro cliente.
Ahora para poder parar el programa tenemos que realizar una lógica para aceptar la palabra “quit”.

Hint: Utilizar cualquiera de las 3 implementaciones de loop vistas.

"""
print("\n *************")
print("Welcome to Disney World!")
print("*************\n ")

print("Buy a ticket, please enter your age")

while True: #para que repita, "el programa debe permanecer vivo".
    age = input(">>> ")
#al poner el input adentro paramos el programa
    if age == "quit": #este if tiene q ir arriba d todo sino no funciona, si encuentra un quit no importa todo lo d abajo
        break  #lo saca del ciclo

    age = int(age) #lo transformamos en int dsps del quit pq sino salta error
    if age < 5: #o sino en ves de eso d ahi arriba podemos poner en cad aif int(age)<5, etc.
        print("Free ticket")
    elif age >= 5 and age <9: #lo mismo q 5 <= age < 9
        print("Ticket fee: U$s 15")
    elif age >= 9 and age < 14:
        print("Ticket fee: U$s 25")
    elif age >= 14 and age < 100:
        print("Ticket fee: U$s 35")
    else:
        print("Your awesome!! Free ticket for you")


#Ejercicio 2
"""
Tomando como base el ejercicio anterior, vamos a analizar qué pasa si a nuestro programa
le ingresamos un carácter no numérico. El programa sigue “vivo” o no? Debatir esta
cuestión.
Utilizando lo aprendido de manejo de excepciones, “salvar” o dicho de manera más formal,
manejar la excepción y mostrar al usuario el siguiente texto “You can't enter
letters. Just numbers greater 0”
"""

#vemos q error tira para saber q excepcion poner

print("\n *************")
print("Welcome to Disney World!")
print("*************\n ")

print("Buy a ticket, please enter your age")

while True:
    age = input(">>> ")
    if age == "quit":
        break

    try: #le dice "vos intneta hacer esto, pero si salta ese error imprimi esto"
        age = int(age)
        if age < 5:
          print("Free ticket")
        elif age >= 5 and age <9:
            print("Ticket fee: U$s 15")
        elif age >= 9 and age < 14:
            print("Ticket fee: U$s 25")
        elif age >= 14 and age < 100:
            print("Ticket fee: U$s 35")
        else:
            print("Your awesome!! Free ticket for you")
    except ValueError:
        print("You can't enter letters. Just numbers greater 0")


#Ejercicio 3
"""
Ejercicio 3:
Una farmacia muy concurrida realiza pedidos una vez por semana a diferentes proveedores
de medicamentos. Nos comenta el dueño que muy a menudo las listas que son realizadas
por diferentes empleados en un excel, tienen productos repetidos. Por lo cual terminan
pidiendo más de lo que deberían y en muchos casos el doble, hay ciertos medicamentos
que la fecha de vencimiento es acotada, por lo tanto en algunos casos finalizan desechando
el medicamento.
El dueño de la farmacia nos contrata para solucionar este problema. Desde nuestro punto
de vista técnico se nos ocurre desarrollar un programa que les permita ingresar los
medicamentos con las siguientes características:
● Medicamento
● Laboratorio
● Cantidad
Si el medicamento ya existe, es decir que está registrado en la lista de la orden, mostrar al
usuario un mensaje que diga “Medicamento existente”.
Ya que estamos haciendo un programa que se mantenga ejecutando, tener presente que
siempre tenemos que contar con una opción para poder parar nuestro programa.
Vamos a permitir que los usuarios puedan listar todos los medicamentos que fueron
cargados, puede ser visualizado en una línea o de preferir darle formato. Esto mismo sirve
"""
print("\n ------------------- Ejercicio 3")
print("\n")

orders = []

while True:
    print("Farmacia - Opciones ")
    print("\n1) Agregar")
    print("\n2) Listar")
    print("\n3) Salir")

    option = input(">> ")
    if option == "3":
        break

    # todo tiene q estar identado, con tab, para q entre en el while

    if option == "1": #identamos todo eso abajo para q este adentro del if

        item = {}

        print("Nombre del medicamento")
        medicine = input(">> ") #a el le gusta poner el input con las flechitas y print
        print("Nombre del laboratorio")
        lab = input(">> ")
        print("Cantidad")
        quantity = input(">> ")

        item["Medicamento"]= medicine
        item["Laboratorio"] = lab
        item["Cantidad"] = quantity

   #     for order in orders:
    #        if order["Medicamento"] == item["Medicamento"]:
     #           print(f"Medicamento exsitente - {order}")
      #   #para q no agregue ese medicamento a la lista
       #     else:
        #        orders.append(item)
    #al final no lo hizo asi

        if item in orders:
         print("Medicamento existente")
        else:
         orders.append(item) #em no me hace nd

    elif option == "2":
        print(f"\nÓrdenes: {orders}")

    else:
        print(f"La opción {option} no es válida")


#RODRIGO:
"""
print("\n++++++++++++++++++++++++")
print("WELCOME TO DISNEY WORLD")
print("++++++++++++++++++++++++\n")

print("Buy a ticket, please enter your age")

while True:
    age = input(">> ")
    if age == "quit":
        break

    age = int(age)

    if age < 5:
        print("Free ticket")
    elif age >= 5 and age < 9:
        print("Ticket price: U$s 15")
    elif age >= 9 and age < 14:
        print("Ticket price: U$s 23")
    elif age >= 14 and age < 100:
        print("Ticket price: U$s 35")
    else:
        print("Your awesome!! Free ticket for you")

print("PROGRAMA FINALIZADO")
"""
"""
print("\n++++++++++++++++++++++++")
print("WELCOME TO DISNEY WORLD")
print("++++++++++++++++++++++++\n")

print("Buy a ticket, please enter your age")

while True:
    age = input(">> ")
    if age == 'quit':
        break

    try:
        if int(age) < 5:
            print("Free ticket")
        elif int(age) >= 5 and int(age) < 9:
            print("Ticket price: U$s 15")
        elif int(age) >= 9 and int(age) < 14:
            print("Ticket price: U$s 23")
        elif int(age) >= 14 and int(age) < 100:
            print("Ticket price: U$s 35")
        else:
            print("Your awesome!! Free ticket for you")
    except ValueError:
        print("You can't enter letters. Just numbers greater 0")

print("PROGRAMA FINALIZADO")
"""
"""
orders = []

while True:
    print("Farmacia - Opciones:")
    print("\t(1) Agregar")
    print("\t(2) Listar")
    print("\t(3) Salir")

    option = input(">> ")
    if option == "3":
        break

    if option == "1":
        item = {}

        print("Nombre del medicamento")
        medicine = input(">> ")

        print("Nombre del laboratorio")
        lab = input(">> ")

        print("Cantidad")
        quantity = input(">> ")

        item['medicamento'] = medicine
        item['laboratorio'] = lab
        item['quantity'] = quantity

        if item in orders:
            print("Medicamento existente")
        else:
            orders.append(item)

    elif option == "2":
        print(f"\nOrdenes: {orders}")

    else:
        print(f"La opcion ({option}) no es valida")

"""

#EJ 4 TAREA, PLANTEAR 5 (dificil)