"""
from flask import Flask #flask modulo, Flask componente

app = Flask(__name__) #esto se usa siempre

@app.route("/", methods=['GET']) #las cosas con @ son anotations, definimos una ruta de nuestra ai. el valor es lo q está
#entre comillas y dsps estan los metodos. le deicmos  a flaks q genere un endpoint /. si algun cliente consulta con este metodo
#flask ejecuta la funcion de abajo de ese route.
def hello_world():
    return "<p>Hello, World!</p>"
"""
#second api del repositorio de rodrigo, ejemplo de crear una api, el de arriba mas simple

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def person():
    rsp = {
        'id': 123,
        'name': "Edgard",
        'is_alive': True,
        'favorite_sports': ['cycling', 'tennis', 'swimming'],
        'graduated': None
    }
    print(type(rsp))
    return rsp #retorna el diccionario


@app.route("/create", methods=['POST']) #aca el endpoint es create, con el metodo http post (para la generacion de cosas dentro del backend)
def new_person():
    print(request.json) #request tiene tod lo relacionado al request d un cliente, obtenemos solo la data del json dentro del request q es lo q escribimos nosotros
    #print(request.method)
    #print(request.url)
    #print(request.data)

    return request.json

@app.route("/personas", methods=['POST', 'GET']) #acá funcionan ambos metodos
def person():
    print(request.json)
    return(request.json)