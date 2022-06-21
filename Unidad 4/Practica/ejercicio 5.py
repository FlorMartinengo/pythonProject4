
usuario_1 = {"user_id": "flor", "pass": "lol"}
usuario_2 = {"user_id": "cata", "pass": "lolazo"}

accounts = [usuario_1, usuario_2]

while True:

    print("Banco Digital")
    user_id = input(">> ")
    password = input (">> ")

    for account in accounts:
        if account["user_id"] == user_id and account["pass"] == password: #es con and pq se tienen q cumplir ambas cosas
            usuario_active = account

    if usuario_active:
        while True:
            print("Usuario logueado")

        # acá mostramos el menú d usuario (con las opciones), sino usuario no válido
    else:
        print("Usuario no válido")