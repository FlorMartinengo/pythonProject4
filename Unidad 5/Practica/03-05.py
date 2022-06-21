
#Ejercicio 2

#una forma con lista d diccionarios, pero es una solucion más compleja de lo necesario
"""vehiculos = [{"categoria": moto, "precio": 10},
             {"categoria": auto, precio: 20},
            {"categoria": camioneta, "precio": 25},
            {"categoria": camion, "precio": 60},
            {"categoria": camion_acoplado, "precio": 90},
             ]
con esta forma habria q usar for
             """
#otra forma con solo un diccionario, mas simple

vehiculos = {
    "moto": 10,
    "auto": 20,
    "camioneta": 25,
    "camion": 60,
    "camion con acoplado": 90,
    "emmet brown": 200
}

def imprimir_ticket(categoria):
    try:
        precio_vehiculo = vehiculos[categoria]
        print("Imprimiendo...")
        print(f"Vehiculo {categoria.upper()}, tarifa: ${precio_vehiculo}")
    except KeyError:
        print(f"No se puede encontrar la categoria {categoria}")
        #ponemos esto por si sale error

def user_menu():
    while True:
        print("1- Moto")
        print("2- Auto")
        print("3- Camioneta")
        print("4- Camion")
        print("5- Camion con acoplado")
        print("6- Emmet Brown")

        option = input(">> ")

        if option == "1":
            imprimir_ticket("moto")
        elif option == "2":
            imprimir_ticket("auto")
        elif option == "3":
            imprimir_ticket("camioneta")
        elif option == "4":
            imprimir_ticket("camion")
        elif option == "5":
            imprimir_ticket("camion con acoplado")
        elif option == "6":
            imprimir_ticket("emmet brown")
        elif option =="quit":
            break

        else:
            print("Opcion invalida")

user_menu()

#Ejerciccio 4
#menu con ingredientes... llama a receta..

recipes = [
    {'recipe': 'Arroz con Verduras', 'ingredients': ['arroz', 'cebolla', 'morron', 'zanahoria', 'castañas', 'zuchini']},
    {'recipe': 'Ensalada de Quinoa', 'ingredients': ['quinoa', 'huevo', 'cebolla morada', 'tomate', 'morron', 'almendras']},
    {'recipe': 'Carne al Horno', 'ingredients': ['colita', 'papa', 'zanahoria', 'batata', 'cebolla', 'ajo']},
    {'recipe': 'Fideos al Pesto', 'ingredients': ['fideos', 'queso', 'nueces', 'albahaca', 'ajo', 'aceite de oliva']},
    {'recipe': 'Guiso de Lentejas', 'ingredients': ['lentejas', 'cebolla', 'zanahoria', 'papa', 'carne', 'puerro', 'morron']},
]

ingredients = [] #hago lista d ingredientes para ir agregando los ing q el usuario pone

def recipe_recommender(): #al haber muchaslistas hay q usar mucho for
   recommend_recipes = []
   for input_ingredient in ingredients:
        for recipe_dict in recipes:
            for recipe_ingredients in recipe_dict["ingredients"]:
                if recipe_ingredients == input_ingredient: #los ingredientes agregados estan en la receta devolver la receta
                    if not(recipe_dict in recommend_recipes): #para q no haya duplicados
                        recommend_recipes.append(recipe_dict)

    return recommend_recipes
#para q en vez d devolver "Receta NONE", devuelva lista vacia

def print_recipes(recipes):
    for recipe in recipes:
        print(f"Receta: {recipe['recipe']}")
        for ingredient in recipe['ingredients']:
            print(f"\t") #no llegue a copiar todo:)

def main_menu():
    print("\n----------------")
    print("¿Qué cocino hoy?")
    print("----------------\n")

    while True: #siempre, para q se mantenga vivo el programa
        print("(1)- Agregar ingrediente")
        print("(2)- Buscar receta")
        print("(3)- A cocinar...") #para salir del programa

        option = input(">> ")

        if option == "1":
            ingredient = input("\tIngrediente: ") #\t es un tab
            #aca el programa se corta para q agregue el ingrediente
            ingredients.append(ingredient)
        elif option == "2":
            if len(ingredients) >= 2:
                recipe = recipe_recommender()
                print_recipes(recipe)
            else:
                print("Debes ingresar al menos 2 ingredientes")
        elif option == "3":
            break
        else:
            print("Opcion inválida")

main_menu() #hay q llamarlo sino no devuelve nd
