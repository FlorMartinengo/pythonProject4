import random
import requests

url = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"
http_rsp = requests.get(url)
print(http_rsp.text)
print(type(http_rsp.text))

#se demora un rato pq la data la va a buscar a un servidor de internet.
#lo queremos en formato json:

print(http_rsp.json())
print(type(http_rsp.json()))
#lo ve como una lista, entonces podemos usar for:

for book in http_rsp.json():
    print(f"Book name: {book['name']}")
    print(f"City name: {book['city']}")

class Novela:
    def __init__(self, titulo, origen):
        self.id = random.randint(0,1000000) #q genere un numero random de 1 a 1m
        self.titulo = titulo
        self.origen = origen

    def __str__(self):
        return f"\n || Novela ||" \
               f"\tTitulo :{self.titulo}\n" \
               f"\tOrigen: {self.origen}\n"

novelas_rsp = http_rsp.json()

novelas = []

for novela in novelas_rsp:
        novela_obj = Novela(novela["name"], novela["city"])
        print(novela_obj)

    #me da error .-.

for novela in novelas_rsp:
       novelas.append(Novela(novela["name"], novela["city"]))



def user_menu():
    print(novelas)

    while True:
        print("1. Listar novelas")
        print("2. Agregar novela")
        print("3. Salir")

        option = input(">> ")

        if option == "1":
            for novela in novelas:
                print(novela)
        elif option == "2":
            print("Nueva novela")
            titulo = input("Titulo: ")
            origen = input("Origen: ")

            mi_novela = Novela(titulo, origen)
            novelas.append(mi_novela)

        elif option == "3":
            break
        else:
            print("Ingrese una opción válida")