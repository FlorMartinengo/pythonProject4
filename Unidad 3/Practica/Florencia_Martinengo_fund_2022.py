"""
"Ejercicio 6:

Estamos participando en el desarrollo de un sistema bancario. Sabemos que hoy en día el
gran volumen de operaciones de compraventa se realizan por medios digitales, entre ellos
están los más tradicionales (tarjeta de débito y crédito) y los más modernos (código QR,
crypto, etc.)
En este proyecto vamos a trabajar con los medios tradicionales, por lo tanto vamos a
suponer que nos envían un archivo en “csv” (investigar), y con el mismo lo convertimos en
una lista de diccionarios. Por lo tanto cada elemento de la lista es un cliente con sus datos
de transacción.
Todas las noches el sistema tiene que correr un proceso, que llamaremos cron job
(investigar), el cual recibe una lista de user_id, la cual representa a clientes que han
realizado un pago a su tarjeta en el día de la fecha. Por ejemplo, si el cliente “1234” contaba
con financiación de 6 cuotas totales, el sistema tiene que incrementar en uno la cuota
actual. Si el cliente lleva pagas 2 cuotas luego de correr el proceso llevará paga 3 cuotas.

Por consiguiente se nos pide los siguientes features del sistema:

● Tomar una lista con user_id llamada “customer_payments” y buscar cada cliente
en la lista de diccionarios que llamaremos “cards_trx”. Si encontramos al cliente
incrementar uno el valor de la key “current_installment”. Pero tener cuidado
ya que el listado de “cards_trx” puede contar con operaciones realizadas con
tarjeta de débito, las cuales para dicho fin tenemos que omitirlas. Buscar la forma de
que no nos afecte la logia de nuestro programa. Luego podemos ver el resultado de
toda la lista y chequear que los valores sean lo que esperamos.

● Definir una variable “remaining_installment” y calcular cuantas cuotas restan para
pagar. Usando la función “print()” mostrar por consola/pantalla el “user_id” y
la cantidad de cuotas que resta pagar.

● Seguido almacenar los “user_id” de aquellos clientes que han cumplido su pago
total y mostrar por pantalla/consola.

● Utilizando “print(---)” y “\n” darle una estructura prolija y legible.
cards_trx

"""

cards_trx = [{'user_id': '35465', 'total_amount': 30000, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment': 7},
{'user_id': '23423', 'total_amount': 19099, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment': 3},
{'user_id': '82312', 'total_amount': 15500, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment': 4},
{'user_id': '29332', 'total_amount': 90200, 'payment_method':
'credit card', 'total_installments': 6, 'current_installment': 4},
{'user_id': '82231', 'total_amount': 29000, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment': 9},
{'user_id': '76289', 'total_amount': 42300, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment': 11},
{'user_id': '58092', 'total_amount': 18900, 'payment_method':
'credit card', 'total_installments': 6, 'current_installment': 1},
{'user_id': '30943', 'total_amount': 13520, 'payment_method': 'debit card'},
{'user_id': '75230', 'total_amount': 67000, 'payment_method':
'credit card', 'total_installments': 6, 'current_installment': 4},
{'user_id': '20582', 'total_amount': 21500, 'payment_method': 'credit card',
 'total_installments': 12, 'current_installment': 6},
{'user_id': '10943', 'total_amount': 5200, 'payment_method': 'debit card'},
{'user_id': '29002', 'total_amount': 9000, 'payment_method': 'credit card', 'total_installments': 12,
 'current_installment': 11},
{'user_id': '92389', 'total_amount': 39200, 'payment_method': 'debit card'},
{'user_id': '12772', 'total_amount': 65700, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment':10},
{'user_id': '72879', 'total_amount': 7300, 'payment_method':
'credit card', 'total_installments': 6, 'current_installment': 5},
{'user_id': '83489', 'total_amount': 44000, 'payment_method': 'debit card'}]

customer_payments = ['23423', '58092', '75230', '72879', '82231', '35465', '30943', '12772']

print("\n")
print("-----")
print("Punto 1")

for card in cards_trx:
    if card["payment_method"] != "debit card":
        if card["user_id"] in customer_payments:
            card["current_installment"] += 1

print(cards_trx)

print("\n")
print("-----")
print("Punto 2")

remaining_installment = []
for n in cards_trx:
    if n["payment_method"] != "debit card":
        cuotas_que_deben = {}
        cuotas_que_deben["user_id: " + n["user_id"]] = ("remaining_installment: " + str((n["total_installments"] - n["current_installment"])))
        remaining_installment.append(cuotas_que_deben)
print(remaining_installment)

print("\n")
print("-----")
print("Punto 3")

payed_all = []

for n in cards_trx:
    if n["payment_method"] != "debit card":
        if (n["total_installments"] - n["current_installment"]) == 0:
            payed_all.append(n["user_id"])
print("El unico que pago el total de cuotas fue el user_id: " + str(payed_all))

