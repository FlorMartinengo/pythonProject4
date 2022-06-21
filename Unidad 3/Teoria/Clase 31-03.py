
#Si tengo muchos elementos repetidos y quiero dejar 1 elemento de cada uno.

#numeros = ["a","b","a","c","d","b"]

"""
lista = []
while elemento:
    if elemento in lista:
        lista.append(elemento)
    print(elemento)

#lo hice mal lol, no se usar while

#habria q usar conjuntos:

c = {}
while e:
    c.add(e)

lista = []
tupla = ()
conjuntos ={}
"""
"""
# UNIDAD 03.D06

# Tuplas

print('\n\n---[Diapo 06]---------------------')

frutas = ('manzana', 'mandarina', 'naranja')

print('Las mandarina están en la posición:', frutas.index('mandarina'))

# print('Las peras están en la posición:', frutas.index('peras'))      # Error!!


frutas = ('manzana', 'mandarina', 'naranja', 'mandarina')

print('Las mandarinas están', frutas.count('mandarina'), 'veces')
print('Las mandarinas están', frutas.count('peras'), 'veces')

print('Las mandarina están en la posición:', frutas.index('mandarina'))

print('\n\n---[Diapo 06 - consulta]---------------------')

frutas = ('manzana', 'no_es_mandarina', 'naranja', 'mandarina')

print('Las mandarinas están', frutas.count('mandarina'), 'veces')
print('Las mandarinas están', frutas.count('peras'), 'veces')


print('Las mandarina están en la posición:', frutas.index('mandarina'))
"""

"""
Seguimos con la diapo de conjuntos
"""



# UNIDAD 03.D07 - D08

# Set - Conjuntos

print('\n\n---[Diapo 07]---------------------')
print('Conjunto vacío:')

frutas = set()

print('El contenido del conjunto es:', frutas)
print('Y el tipo de dato es:', type(frutas))


print('\nConjunto con elementos:')

frutas = {'manzana', 'naranja', 'pera'}

print('El conjunto contiene:', frutas)

frutas.add('mandarina')
print('Y ahora:', frutas)


print('\n\n---[Diapo 07.a]---------------------')
print('Agregamos elementos repetidos:')

frutas = {'manzana', 'naranja', 'pera', 'pera', 'pera'}

print('Contenido de frutas:', frutas)

frutas.add('manzana')
frutas.add('pera')


print('Y ahora:', frutas)

#Si quisieras agregar un elemento q ya esta t acepta la operación pero t deja el conjunto igual (arriba se ve)

print('\n\n---[Diapo 08.b]---------------------')
print('Un Truco! Cómo eliminar elmentos duplicados en listas? ...')

frutas = ['manzana', 'pera', 'naranja', 'pera', 'pera']

print('Frutas: ', frutas)

conjunto = set(frutas)
frutas = list(conjunto)

print('Y ahora: ', frutas)
#Creas un conjunto de la lista set(lista) y dsps del conjunto crear otra lista

print('\n\n---[Diapo 09.a]---------------------')
print('Eliminar elementos de un conjunto:')

frutas = {'manzana', 'naranja', 'pera'}
print('Contenido de frutas:', frutas)

frutas.remove('naranja')
print('Y ahora:', frutas)


print('\n\n---[Diapo 09.b]---------------------')
print('Pertenece a un conjunto')

frutas = {'manzana', 'naranja', 'pera'}
print('Contenido de frutas:', frutas)

print('\n in ')

print('Está la naranja?:', 'naranja' in frutas)
print('Está la mandarina?:', 'mandarina' in frutas)

print('\n not in ')

print('No está la naranja?:', 'naranja' not in frutas)
print('No está la mandarina?:', 'mandarina' not in frutas)

#BREAKPOINTS
""" DEBUG, poner un break point tocando al lado del numero de la fila ,y dsps usar el boton bichito al lado del play"""

#funciona lo de in y not in tmb en listas
hola =["si", "no"]
print("Esta si?", "si" in hola)

# UNIDAD 03.D25 - D27

# Diccionarios

print('\n\n---[Diapo 25]---------------------')
print('Diccionarios:')

diccio = {
    'naranja': 'orange',
    'manzana': 'apple',
    'pera': 'pear'
}

print('Diccionario', diccio)
print('Manzana en inglés se dice: ', diccio['manzana'])

print('\nCon claves numéricas: ')
diccio = {
    10: 'diez',
    5: 'cinco',
    1: 'uno'
}

print('Diccionario:', diccio)
print('El valor de la clave 1 es:', diccio[1])


print('\n\n---[Diapo 26.a]---------------------')
print('Los diccionarios son mutables:')

diccio = {
    'naranja': 'orange',
    'manzana': 'apple',
    'pera': 'pear'
}

print('Manzana en inglés se dice: ', diccio['manzana'])

diccio['manzana'] = 'banana'
print('Manzana en inglés ... ahora se dice: ', diccio['manzana'])


print('\n\n---[Diapo 26.b]---------------------')
print('Agregar y eliminar elementos a los diccionarios')

diccio = {
    'naranja': 'orange',
    'manzana': 'apple',
    'pera': 'pear'
}

print('Diccionario ', diccio)

# Eliminar
del(diccio['manzana'])
print('Diccionario ', diccio)

# Agregar
diccio['sandia'] = 'watermelon'
print('Diccionario', diccio)

