
#contraseña "ofuscada" password: ******, con getpass.getpass
# http://pymotw.com/2/getpass/

#importamos modulo, siempre al principio los imports.

"""
import getpass

p = getpass.getpass() #dentro del modulo tenemos metodos, en este caso tmb getpass
print("You entered:", p)
"""

#em a mi no me hace nada a el le aparece, Password: You entered: lo q escribio
"""
si apreto ctrl y hovereo sobre las cosas me lleva a explicaciones

prompt y stream, dice q es 13:24, investigar igual

ejercicos de ford y d blockbuster los más interesantes, más ricos
"""

#WARM UP U6
"""Con el objetivo de familiarizarnos con el paradigma de programación orientada a objetos,
vamos a comenzar con un diseño muy simple del mundo real. Recordemos que los
paradigmas nos proveen principios para poder luego estructurar nuestra comprensión y
solución de la problemática.
Vamos a desarrollar un programa en el cual, definiremos una clase “Ballena”, la cual va
a contar con los siguientes atributos:
● Nombre
● Edad
● Sexo
● Peso
● Mamifero
Definiendo estos atributos de clase, utilizar el método constructor “__init__()”.
Seguido, crear una instancia de la clase y asignar el nombre “Willy”, guardar la instancia en
un variable. Hasta acá bien, pero pensemos que “Willy” además de tener atributos, cuenta
con acciones. Por lo tanto definir los métodos, “nadar”, “saltar”, “alimentarse”
y “descansar”. Cada uno de los métodos deberá imprimir un mensaje con
pantalla/consola. Ejemplo: “{name}, está nadando…”.
Finalmente vamos a definir otro método que se llame “estado”, el cual devolverá de forma
prolija todos los atributos de “Willy” o cualquier otra ballena que hayamos creado.
Test: Realizar la siguiente prueba, crear un clon de “Willy” y guardarlo en otra variable.
Luego utilizar la condición “if” para saber si son iguales. Debatir esto en clase."""

class Ballena:
    def __init__(self, nombre, edad, sexo, peso, mamifero):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.mamifero = mamifero

#acá ya tenemos nuestro constructor. vamos a probarlo:

Willy = Ballena("Willy", 9, "M", 2000, True) #2000kg, 2 toneladas
print(f"Mi ballena es: {Willy}")

# devuelve esto Mi ballena es: <__main__.Ballena object at 0x0000024E02071BA0>
#ese numero es la direccion de memoria, la identificacion. no nos interesa ver eso
#con dot.notation, pongo un punto y traigo los atributos

print(f"Mi ballena es: {Willy.nombre}")

# ahora crear metodos, acciones para la clase. definir metodos tmb con def, dentro de Class

print("\n")

class Ballena2:
    def __init__(self, nombre, edad, sexo, peso, mamifero):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.mamifero = mamifero

    def nadar(self):
        return f"{self.nombre} está nadando..."
    def saltar(self):
        return f"{self.nombre} va a saltar la escollera..."
    def alimentarse(self):
        return f"{self.nombre} está alimentándose..."
    def descansar(self):
        return f"{self.nombre} zzzZZZzzzZzZZZZZzzz..."

Willy2 = Ballena2("Willy", 9, "M", 2000, True)

print(Willy2.nadar())
print(Willy2.saltar())
print(Willy2.alimentarse())
print(Willy2.descansar())

#definimos clase ballena, sus atributos y definimos esos 4 métodos
#ahora "estado":

class Ballena3:
    def __init__(self, nombre, edad, sexo, peso, mamifero):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.mamifero = mamifero

    def nadar(self):
        return f"{self.nombre} está nadando..."
    def saltar(self):
        return f"{self.nombre} va a saltar la escollera..."
    def alimentarse(self):
        return f"{self.nombre} está alimentándose..."
    def descansar(self):
        return f"{self.nombre} zzzZZZzzzZzZZZZZzzz..."
    def estado(self):
        return f"\n\tNombre: {self.nombre} " \
               f"\n\tEdad: {self.edad} " \
               f"\n\tSexo: {self.sexo} " \
               f"\n\tPeso: {self.peso} " \
               f"\n\tEs mamifero: {'SI' if self.mamifero else 'NO'}"

Willy3 = Ballena3("Willy", 9, "M", 2000, True)
print(Willy3.estado())

print("\n")
#Hacer clon de Willy

Willy_clone = Ballena3("Willy", 9, "M", 2000, True) #variable q adentro tiene un objeto

print(Willy_clone.estado()) #devuelve lo mismo. esto es lo bueno d los moldes, podemos crear muchas.
# heredan sus atributos y métodos

print(Willy3 == Willy_clone) #no son iguales, son objetos diferentes. son representaicone siguales, pero son diferentes sectores de la memoria
print(Willy3.nombre == Willy_clone.nombre) #tienen el mismo nombre, compara los strings "Willy" vs "Willy"

print(Willy3)
print(Willy_clone) #lol a mi me da el mismo nro Object at "...", a el distinto

Willy_clone_2 = Willy_clone #variable igualada a otra variable q es un objeto. aca si son iguales
print(Willy_clone_2 == Willy_clone)
#si cambia Willy_clone, Willy_clone_2 tmb cambia, Willy_clone y Willy 3 tienen los mismo atributos pero son diferentes

"""Cada objeto tiene una entidad. cada objeto es diferente"""

#EJERCICIO 1 U6
"""
Quién hubiese dicho hace 10 años que las impresoras (papel y tinta) iban a evolucionar en
lo que conocemos como impresora 3D. Ojo eso no quiere decir que las impresoras
tradicionales sean obsoletas, sin duda son una gran herramienta de trabajo… al menos
hasta el momento. Aunque con la aceptación de la digitalización en diferentes rubros está
poniendo en jaque el uso de las mismas. Y bueno, ya que la producción de papel tiene un
impacto ambiental bastante considerable, que así sea.
Estamos trabajando en una compañía de Diseño y nuestro
equipo recibe una impresora 3D. La cual como nos
encontramos ejecutando un proyecto de bloques
interactivos para niños, decidimos escribir un programa
que defina 3 figuras geométricas (esfera, cubo y prisma
rectangular). Cada figura tendrá sus características que
denominaremos atributos. Utilizando el paradigma de
POO, escribir el siguiente programa.
● Definir 3 clases, una para cada figura geométrica
○ Esfera, tendrá como propiedad “nombre” y “radio”
○ Cubo, tendrá como propiedad “nombre”, “lado”
○ Prisma rectangular, tendrá como propiedades ”nombre”, “base”, “altura” y
“profundidad”
○ NOTA: el nombre será un propiedad definida por defecto en la clase
Ing. Rodrigo Sellanes
● Definir los siguientes métodos para cada clase
○ Esfera, tendrá 2 métodos, uno que devuelva el nombre de la figura y otro el
radio
○ Cubo, tendrá 2 métodos que devolverá el nombre de la figura y otro el lado
○ Prisma rectangular, tendrá 2 métodos que devuelva el nombre y otro la base,
altura y profundidad en un array, en ese orden.
● Migrar las 3 clases a un modulo que llamaremos “shapes.py” luego importar este
modulo a nuestro archivo “main.py”.
● En el archivo “main.py” generar un “user_menu()” que pregunta cuál de las 3
figuras geométricas quiere imprimir en 3D. Luego crear una función que imprima por
pantalla/consola cual figura geométrica se está imprimiendo, utilizar el mensaje
“Imprimiento…{shape.name} por favor espere”.
● Agregar un método en cada uno de las figuras geométricas denominado
“print_properties” el cual imprima por pantalla/consola el nombre de la figura
y sus características. Eso nos facilitará la impresión por pantalla/consola de las
dimensiones de nuestras figuras.
● Finalmente agregar un nuevo método “print_3d” en cada una de las clases.
Llamar a este método cuando el usuario quiere imprimir una figura.
"""

#lo hizo 14:20 chau me fui a estudiar micro

