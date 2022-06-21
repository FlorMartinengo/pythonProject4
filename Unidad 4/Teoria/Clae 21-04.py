
def dias_semana():
    return ["Lunes", "Martes", "Sabado", "Domingo"]

print("Fin de semana: ", dias_semana()[2:]) #hay q poner los parentesis antes d los corchetes


def multiples_retornos():
    return "Hola", "Mal"
print(multiples_retornos())
print(type(multiples_retornos()))

def multiples_retornos2():
    return "Hola", 2, True, [3,4,5]
print(multiples_retornos2())
print(type(multiples_retornos2()))

def multiples_retornos3():
    return ["Hola", "Mal"]
print(multiples_retornos3())
print(type(multiples_retornos3()))

def multiples_retornos4():
    return ["Hola", 1, True, [1,2,3]]
print(multiples_retornos4())
print(type(multiples_retornos4()))

primero, segundo, tercero, cuarto = multiples_retornos2()
print(primero)
print(segundo)
print(tercero)
print(cuarto)


#EJERCICIO 5 - TP4
"""
Acreditar--> corriente y caja de ahorro
Consultar--> saldos y transacciones
Login
Salir-->Cerrar y borrar
Menu
"""

print("\n -------- Ejercicio 5 \n")
while True:
    user = input("Ingresar su ID: ")
    password = input("Ingresar clave: ")
    cuenta = funcion_login(user, password) #para saber si esta bn, si tiene cuenta en el banco
    #para esto necesito saber la base de datos del banco
  #nosotros tenemos q hacer la base de datos :)))))
    if cuenta != {} #la cuenta no está vacia, es del banco
        opciones = int(input("Opcion"))
        while opciones >= 1 and opciones <= 6 #o sino con conjuntos: opciones in [1,2,3,4,5,6] #yo lo haria con un if y nada al lado del while
            if opciones == 3:
                fun_saldo_ca(cuenta) #hacer esta funcion tmb aparte (p.modular, si hariamos td en el mismo lugar seria procedural)
                #def fun_saldo_ca(cuenta)-> ...->print("Saldo: ..")
            if opciones == 1: #o usar elif es lo mismo
                fun_acreditar_ca(cuenta) #def....-> print(acreditado)
            if opciones == 6:
                fun_salir() #fun_salir()-->cuenta = {}->user=""->password="" , esto para "desconectar" el usuario anterior
                break #salimos del segundo while entonces vuelve al primer while, vuelve a pedir el usuario



