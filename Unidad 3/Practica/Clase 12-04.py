
#13:07 empieza a hacer un repaso hasta 13:26
"""
# Variables (string, boolean, number (int o float)
# Lista ['string', boolean, 1, 2, [...], ...] --> index 0 - N --> len(lista)
# Diccionarios {k: v}
# Tupla ('rodri'), Conjunto {1, 2, 3, 4}

# funciones del lenguaje: len(), print(), int("1"), float("1.2")


# RUNNING -> TOP -> BOTTOM

botellas = ['vidrio', {'botella': 'plastico'}, ['acero']]

for botella in botellas:
    print(f"Tipo de dato: {type(botella)}")
    print(f"Valor: {botella}")

"""
#13:32 hace ej 5

# Ejercicio 5 | cities

eeuu = {
    "country": "Estados Unidos",
    "cities": ['New Your', 'Miami'],
    "currency": "U$s",
    "language": "Ingles"
}

costa_rica = {
    "country": "Costa Rica",
    "cities": ['San Jose', 'Santa Teresa'],
    "currency": "CRC",
    "language": "Español"
}

mexico = {
    "country": "Mexico",
    "cities": ['Acapulco', 'DF'],
    "currency": "MX",
    "language": "Español"
}

countrys = [eeuu, costa_rica, mexico]
suecia_ok = False
df_exist = False
vist_cities = []

for country in countrys:
    if country['country'] == 'Suecia':
        suecia_ok = True

    print(country.get("vacations", "No existe la clave vacations"))

    for city in country['cities']:
        vist_cities.append(city)
        if city == 'DF':
            print(f"La ciudad DF existe en destinos a visitar - {city}")

print(f"Existe Suecia: {suecia_ok}")
print(f"Todas las ciudades a visitar: \n {vist_cities}")


#hasta las 14:38, ahora avanza al ejercicio 7 hasta 14:55

# Ejercicio 7 | Random

numbers = []

for number in range(101):

    if number == 0:
        print(f"NUMBER TO AVOID: {number}")
        continue

    number_dict = {}
    number_dict['number'] = number

    if number % 2 == 0:
        number_dict['type'] = "par"
    else:
        number_dict['type'] = "impar"

    numbers.append(number_dict)

print(numbers)

#15:00 habla del ej 6, ayuda un poco hasta 15:04