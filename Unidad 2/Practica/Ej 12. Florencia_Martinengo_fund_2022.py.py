
dnis = [37128693, 38346828, 48577851, 23923908, 23747794, 46033685, 28372488, 33143443,
38122921, 38915457, 24807285, 35759559, 21061055, 33613272, 24082600, 26477319,
46655903, 46988530, 25145603, 35368988, 25393784, 21295674, 48348316, 31247247,
28498292, 37538741, 21332845, 27557703, 24435687, 38794110, 44518399, 34178717,
45788239, 36998322, 32098132, 22185788, 25030083, 21256524, 34592517, 41755997,
37570846, 30401721, 34832996, 47330519, 34380715, 42724546, 26615771, 23171192,
42223891, 40210778, 33530381, 20478110, 20753240, 28187999, 27785500, 37236996,
22981717, 27744330, 44855039, 36552090, 36824210, 39684157, 26469844, 45037525,
25916934, 41595563, 23571241, 30552911, 40100736, 36047292, 46818813, 36680587,
36107300, 41367347]

notas = [15, 19, 19, 9, 6, 12, 20, 3, 1, 15, 10, 16, 3, 25, 18, 13, 24, 30, 7, 28, 20, 25, 28, 10, 2, 1,
18, 20, 3, 3, 19, 12, 11, 8, 24, 27, 15, 15, 19, 0, 27, 8, 29, 5, 1, 12, 8, 17, 19, 0, 0, 18, 15,
23, 22, 2, 24, 6, 10, 28, 18, 3, 15, 6, 26, 0, 21, 14, 24, 13, 10, 17, 16, 2]


"""
def mi_nota(numero):
    print(dnis[numero], notas[numero])

mi_nota(42)

Así lo sé hacer, pero no vimos def todavía así que hice otras opciones:
"""
#la idea era hacerlo sin funciones pq no lo vimos todavia.
#en wpp "resoluciones ej 12 info" fotos d como lo hicieron las chicas


print('\n\n----[EJERCICIO 12]----')
print('\n Nota IELTS')
numero = int(input('¿Qué número sos?: '))
print(dnis[numero], notas[numero])

print('\n\n---Categorias--')
avanzado = []
intermedio_alto = []
intermedio_bajo = []
basico = []
debajo_basico = []

for nota in notas:
    if nota >= 25:
        avanzado.append(nota)
    elif 20 <= nota <= 24:
        intermedio_alto.append(nota)
    elif 16 <= nota <= 19:
        intermedio_bajo.append(nota)
    elif 10 <= nota <= 15:
        basico.append(nota)
    else:
        debajo_basico.append(nota)

print(f"Avanzado: {avanzado}")
print(f"Intermedio Alto: {intermedio_alto}")
print (f"Intermedio Bajo: {intermedio_bajo}")
print(f"Basico: {basico}")
print(f"Debajo del básico: {debajo_basico}")

print('\n\n---Cantidad por categoria---')
print(f"Avanzado: {len(avanzado)}")
print(f"Intermedio Alto: {len(intermedio_alto)}")
print (f"Intermedio Bajo: {len(intermedio_bajo)}")
print(f"Basico: {len(basico)}")
print(f"Debajo del básico: {len(debajo_basico)}")

print('\n---Total de estudiantes que se presentaron---')
total_de_estudiantes= 0
for nota in notas:
    total_de_estudiantes += 1
print(total_de_estudiantes)

""" 
Ó, más facil:
print(len(notas))
"""