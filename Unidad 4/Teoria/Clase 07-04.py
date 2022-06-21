"""
# UNIDAD 03.D31 - D33

# Errores

print('\n\n---[Diapo 31]---------------------')
print('Errores Sintácticos:')


print('Comienzo')
#  articulo = "Pelota
#  print("El artícuo es:", articulo)



print('\n\n---[Diapo 32]---------------------')
print('Errores Semánticos:')

numero = int(input("Ingrese un número:"))
division = 10 / numero
print("Resultado: ", division)




print('\n\n---[Diapo 33]---------------------')
print('Errores Semánticos controlados:')

numero = int(input("Ingrese un número:"))
if numero == 0:
    print("Error: no se puede ingresar un 0!")
else:
    division = 10 / numero
    print("Resultado: ", division)
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
"""

# UNIDAD 03.D34 - D37

# Excepciones con try / Catch

print('\n\n---[Diapo 34.a]---------------------')
print('Errores Semánticos:')

numero = int(input('Ingrese un número:'))
division = 10 / numero
print('Resultado: ', division)



# Try / Except
print('\n\n---[Diapo 34.b]---------------------')
print('Excepciones:')

try:
    numero = int(input('Ingrese un número:'))
    division = 10 / numero
    print('Resultado: ', division)
except:
    print('Error: algo fallo al intentar realizar el cálculo')



# Try / Except
print('\n\n---[Diapo 35]---------------------')
print('Se reintenta hasta que se ingresa ok:')

while True:
    try:
        numero = int(input('Ingrese un número:'))
        division = 10 / numero
        print('Resultado: ', division)
        break
    except:
        print('Error: algo fallo al intentar realizar el cálculo')


print('Fin del Programa de división.')


# Try / Except / Else
print('\n\n---[Diapo 36.a]---------------------')
print('Se reintenta hasta que se ingresa ok:')

while True:
    try:
        numero = int(input('Ingrese un número:'))
        division = 10 / numero
    except:
        print('Error: algo fallo al intentar realizar el cálculo')
    else:
        print('Resultado: ', division)
        break

print('Fin del Programa de división.')





# Try / Except / Else / Finally
print('\n\n---[Diapo 36.b]---------------------')
print('Se reintenta hasta que se ingresa ok:')

while True:
    try:
        numero = int(input('Ingrese un número:'))
        division = 10 / numero
    except:
        print('Error: algo fallo al intentar realizar el cálculo')
    else:
        print('Resultado: ', division)
        break
    finally:
        print('Este bloque se ejecuta siempre')

print('Fin del Programa de división.')




'''
Excepciones Múltiples
Ejemplo con ValueError y ZeroDivisionError
'''
print('\n\n---[Diapo 37]---------------------')
print('Determinando el tipo de excepción:')

while True:
    try:
        numero = int(input('Ingrese un número:'))
        division = 10 / numero
        print('Resultado: ', division)
        break
    except Exception as e:
        print('Error del tipo:', type(e).__name__) #para ser mas preciso y saber d q tipo es el error

print('Fin del Programa de división.')




print('\n\n---[Diapo 38]---------------------')
print('Excepciones múltiples:')

while True:  #while true esq t haga seguir poniendo valores hasta q pongas uno valido
    try:
        numero = int(input('Ingrese un número:'))
        division = 10 / numero
        print('Resultado: ', division)
        break
    except ValueError:
        print('Ingrese un valor numérico')
    except ZeroDivisionError:
        print('Ingrese un valor distinto de 0')
    except Exception as e:
        print('Error del tipo:', type(e).__name__)

print('Fin del Programa de división.')




print('\n\n---[Diapo 39]---------------------')
print('Lanzando a mis propias excepciones:')

try:
    raise ValueError('Error en el valor del dato') #nosotros tiramos las exepciones, raise "nombre de la excepcion"
except Exception as e:
    print('Error de tipo', type(e).__name__, ':', e)

