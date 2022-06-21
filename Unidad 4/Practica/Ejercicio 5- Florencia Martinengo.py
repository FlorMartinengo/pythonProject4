cuentas = [
    {"user_id": "agustin", "password": "agus123",
     "cuenta_ahorro":{"numero_cuenta": "CA-111-111", "cantidad": 100},
     "cuenta_corriente":{"numero_cuenta":"CC-222-222", "cantidad": 100},
    "ultimas_transacciones": []},

     {"user_id": "martina", "password": "martu123",
      "cuenta_ahorro": {"numero_cuenta": "CA-333-333", "cantidad": 100},
      "cuenta_corriente": {"numero_cuenta": "CC-222-333", "cantidad": 100},
      "ultimas_transacciones": []},

     {"user_id": "fermin", "password": "fer123",
       "cuenta_ahorro": {"numero_cuenta": "CA-444-444", "cantidad": 100},
       "cuenta_corriente": {"numero_cuenta": "CC-555-222", "cantidad": 100},
       "ultimas_transacciones": []},

     {"user_id": "adolin", "password": "adol123",
       "cuenta_ahorro": {"numero_cuenta": "CA-555-555", "cantidad": 100},
       "cuenta_corriente": {"numero_cuenta": "CC-666-222", "cantidad": 100},
      "ultimas_transacciones": []},

     {"user_id": "teresa", "password": "tere123",
      "cuenta_ahorro": {"numero_cuenta": "CA-777-777", "cantidad": 100},
       "cuenta_corriente": {"numero_cuenta": "CC-888-888", "cantidad": 100},
      "ultimas_transacciones": []},

    {"user_id": "silvana", "password": "sil123",
     "cuenta_ahorro": {"numero_cuenta": "CA-444-444", "cantidad": 100},
     "cuenta_corriente": {"numero_cuenta": "CC-222-222", "cantidad": 100},
     "ultimas_transacciones": []}
]

ACRED_CA = 1
ACRED_CC = 2
SALDO_CA = 3
SALDO_CC = 4
CONS_TRX = 5
SALIR = 6

def fun_operaciones_disponibles():
    opcion = 0
    while opcion not in [ACRED_CC,ACRED_CA,SALDO_CC,SALDO_CA,CONS_TRX,SALIR]:
        print('\t 1) Acreditar en CA')
        print("\t 2) Acreditar en CC")
        print("\t 3) Consultar saldo CA")
        print("\t 4) Consultar saldo CC")
        print("\t 5) Consultar Transacciones")
        print("\t 6) Salir")
        opcion = int(input("Seleccione una opción: "))

    return opcion

#opcion = fun_operaciones_disponibles()
#print("La opción elegida es: ", opcion)

#Dado el user y la pass, retorna la cuenta de ese usuario. Si hay error retorna un coleccion vacía

def funcion_login(user, password):
    cuenta_encontrada = {}
    print('\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('\t\t @@@  Banco Digital LA @@@')
    print('\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@')

    for cuenta in cuentas:
        if cuenta["user_id"] == user:
            print("Usuario existente")
            if cuenta["password"] == password:
                print("Usuario logueado")
                cuenta_encontrada = cuenta
            else:
                print("Clave errónea")

    return cuenta_encontrada


def funcion_ingresar_cantidad():
    cantidad = 0
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except Exception:
            print("Error con la cantidad")

    print(cantidad)
    return(cantidad)


def funcion_acreditar_ca(cuenta):
    print("Deposito en Caja de Ahorro: ")
    cantidad = funcion_ingresar_cantidad()
    cuenta["cuenta_ahorro"]["cantidad"] += cantidad
    cuenta["ultimas_transacciones"].append(cantidad)


def funcion_acreditar_cc(cuenta):
    print("Deposito en Cuenta Corriente:")
    cantidad = funcion_ingresar_cantidad()
    cuenta["cuenta_corriente"]["cantidad"] += cantidad
    cuenta["ultimas_transacciones"].append(cantidad)

def funcion_saldo_ca(cuenta):
    print("Resumen de CA")
    numero = cuenta["cuenta_ahorro"]["numero_cuenta"]
    saldo = cuenta["cuenta_ahorro"]["cantidad"]
    print("Numero de cuenta: ", numero)
    print("Saldo: La$ ", saldo)
    print("-----------------------")

def funcion_saldo_cc(cuenta):
    print("Resumen de CC")
    numero = cuenta["cuenta_corriente"]["numero_cuenta"]
    saldo = cuenta["cuenta_corriente"]["cantidad"]
    print("Numero de cuenta: ", numero)
    print("Saldo: La$ ", saldo)
    print("-----------------------")

def funcion_transacciones(cuenta, cant):
    print("-----------------------")
    print("Ultimas ", cant, " realizadas: ")
    transacciones = cuenta["ultimas_transacciones"][-cant:]
    transacciones.reverse()
    for transaccion in transacciones:
        print("\t La$ ", transaccion)
    print("-----------------------")

def funcion_salir(user):
    print("Gracias ", user, " por utilizar nuestro Banco Digital.")
    user = ""
    password = ""
    cuenta = {}
    print("Saliendo...")

#ahora dsps de haber hecho todas las funciones, etc, viene el programa en sí
while True:
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su clave: ")

    cuenta = funcion_login(user,password)
    print(cuenta)

    if cuenta != {}:
        opcion = ""

        while opcion != SALIR:
            opcion = fun_operaciones_disponibles()

            if opcion == ACRED_CA:
                funcion_acreditar_ca(cuenta)
            elif opcion == ACRED_CC:
                funcion_acreditar_cc(cuenta)
            elif opcion == SALDO_CA:
                funcion_saldo_ca(cuenta)
            elif opcion == SALDO_CC:
                funcion_saldo_cc(cuenta)
            elif opcion == CONS_TRX:
                funcion_transacciones(cuenta, 3)
            elif opcion == SALIR:
                funcion_salir(user)


