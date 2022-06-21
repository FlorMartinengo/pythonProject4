import requests

#el url hay que ponerlo hasta el igno de pregunta, el resto i=.. son parametros

url = "http://www.thecocktaildb.com/api/json/v1/1/search.php" #tuvimos que agregar el http:// , sino daba error

#del ej 3, el link de gin del link de la pagina de cocktails
#hay muchos servicios, cada una de la surls de la pag es una api distinta, un servicio distinto, q devuelve una data distinta
#esta api especifica que tenes que usar parametros, al final del link dice i=Gin e i=Vodka. la api espera ese parametro

http_rsp = requests.get(url, params={"s": "margarita"})
rsp_json = http_rsp.json()

print(rsp_json)
print(type(rsp_json))

print(rsp_json["drinks"]) #devuelve una lista

print(rsp_json["drinks"][0]["idDrink"])#queremos quedarnos con el id del primer elemento de la lista

#así podemos llamar a cualq cosa de las apis, usamos el primer elemento de la lista para q sea mas facil

class Drinks:
    def __init__(self, title, strAlcoholic, strInstructions): #cada uno elije lo q tiene ganas
        self.title = title
        self.strAlcoholic = strAlcoholic
        self.strInstructions = strInstructions

    def __str__(self):
        return f"{self.title}, {self.strInstructions}, {self.strAlcoholic}"


#hacerlo con input:

base_url = "http://www.thecocktaildb.com/api/json/v1/1/search.php"

print(Drinks("T", "s", "s"))

#supuestamente los objetos se ponen dentro de una carpeta models?

drink_type = input("Drink>> ")
req_params = {"s": drink_type} #req_params es un diccionario

http_rsp = requests.get(base_url, params = req_params)
print(http_rsp.json())


