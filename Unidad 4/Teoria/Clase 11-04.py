
# UNIDAD 03.D13 - D16

#Formateando los datos de salida

print('\n\n---[Diapo 13.a]--------------------------')
# Formateos

nombre = 'Jorge'
apellido = 'Rodriguez'
cadena = 'Mi nombre es {} y mi apellido es {}'.format(nombre, apellido)

print('Cadena: ', cadena)


print('\n\n---[Diapo 13.b]--------------------------')
# Posicional
nombre = 'Jorge'
apellido = 'Rodriguez'
print('Mi nombre es {1} y mi apellido es {0}'.format(nombre, apellido))



print('\n\n---[Diapo 14.a]--------------------------')
# Uso de nombres

nombre = 'Jorge'
apellido = 'Rodriguez'
print('Mi nombre es {n} y mi apellido es {m}'.format(n=nombre, m=apellido))

print('\n\n')

print('Mi nombre es {nombre} y mi apellido es {apellido}'.format(nombre='Jorge', apellido='Rodriguez'))


print('\n\n---[Diapo 14.b y 15]---------------------')
print('Alinenando Textos: \n')

# Derecha
c = '{:>30}'.format('Hola a Todos')
print(c)

# Izquierda
c = '{:30}'.format('Hola a Todos') + 'Fin.'
print(c)

# Centro
c = '{:^30}'.format('Hola a Todos') + 'Fin.'
print(c)

# Truncado
c = '{:.3}'.format('Hola a Todos')
print(c)



print('\n\n---[Diapo 15.b y 16]--------------------------')
print('Rellenando Números: \n')

print('\n Rellenando con espacios a izquierda \n')

print('{:4}'.format(10))
print('{:4}'.format(100))
print('{:4}'.format(1000))

print('\n Rellenando ceros \n')

print('{:04}'.format(10))
print('{:04}'.format(100))
print('{:04}'.format(1000))

print()

print('{:>4}'.format(10))
print('{:>4}'.format(100))
print('{:>4}'.format(1000))

print('\n Truncar Flotantes, y rellenos a izquierda con espacios o ceros: \n')

print('{:.2f}'.format(3.141592))

print()

print('{:7.2f}'.format(3.141592))
print('{:7.2f}'.format(153.21))

print()

print('{:07.2f}'.format(3.141592))
print('{:07.2f}'.format(153.21))

print("\n")

#formateos
#quiero "pi vale 03.14"

pi = 3.14159265
print("pi vale {:>05.2f}".format(3.14159265))

"""
5 espacios (03.14) y 2 numeros flotantes, dsps de la coma
se agrega el 0 adelante para q llene con ceros, sino llena con espacios
el punto/coma del decimal cuenta como un espacio
"""

print("pi vale {:>05.2f}".format(pi))

#se podria sin >

print("\n")

def tabla_multiplicar(num):
    for n in range(10):
        print("{} x {} = {}".format(num,n,n*num))  #distintas formas de hacer esto, con strings ej, sin format.

num = int(input("Número a multiplicar"))
tabla_multiplicar(num)

print("\n")

mensaje= "Hola"

def suma(a,b):
    numero = 24
    print(mensaje)
    print(numero) #usa la variable local (le hace sombra a la otra variable numero)
    return a + b

suma(4,5) #no funca

numero= 22
print(numero) #usa la variable global (le hace sombra a la otra variable numero)