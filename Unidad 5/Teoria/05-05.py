#FACTORIAL- función recursiva
""" como lo hizo el, me da error
def factorial(n):
    if n > 1:
        f = factorial(n-1)*n
        print("factorial("+n+")"+f)
        return f
    if n==1:
        print("factorial(",n,"):1")
        return 1

val = factorial(5)
print(val)

#bomba q explota ejercicio, tmb ejemplo d funcion recursiva (usa la misma funcion q estamos haciendo dentro d la misma funcion)

def bomba(nro):
    if nro > 0:
        print(nro)
        bomba(nro-1)
    else:
        print("BOOOOOOOOOMMMMMM!")

bomba(5)
"""
""" Siento q se podria hacer cn range pero no me sale
def factorial(n):
    if n > 1:
        for num in range(2,n):
            return num*(num-1)

n= factorial(2)
print(n)
"""
"""SACADO DE GOOGLE:
n = 3
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("The factorial of 23 is : ", end="")
print(fact)
"""

lista = [1,2,3,4,5,6,7,8,9,10]

"""Una manera de hacerlo:
def buscar(n,lista):
    for e in lista:
        if e == n:
            return True
    else:
        print("No existe ese número en la lista ingresada")

buscar3 = buscar(3,lista)
print(buscar3)
"""

def buscar(n,lista):
    if len(lista) == 1:
        if lista[0] == n:
            return True
        else:
            return False

    return buscar(n, lista[0:1]) or buscar(n, lista[1:]) #parte la lista en 2

print(buscar(12,lista))
