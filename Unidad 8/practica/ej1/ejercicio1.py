persona = {
  "nombre": "Mike",
  "apellido": "Mathue",
  "sexo": "Male",
  "direccion": "Av. Mugga Way 934",
  "estado": "Canberra",
  "pais": "Australia",
  "gustos_musicales": ["Aerosmith", "Metallica", "Dream Theater", "Deep Purple"]
}

print(persona)
print(type(persona)) #es un diccionario, en pycharm un json tiene la misma
#representacion q un diccionario

#si quisiera dentro de pais pasar nombre y codigo, hacer un diccionario dentro de pais

persona2 = {
  "nombre": "Mike",
  "apellido": "Mathue",
  "sexo": "Male",
  "direccion": "Av. Mugga Way 934",
  "estado": "Canberra",
  "pais": {
   "nombre": "Australia",
    "codigo": "AUS"
  },
  "gustos_musicales": ["Aerosmith", "Metallica", "Dream Theater", "Deep Purple"]
}

#en json tmb funciona

