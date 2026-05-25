convidados = ["Bernado", "Samuel", "Caetano", "Antonio","Pedro"]


convidados[2] = "Lucas"


convidados.append("Joaquin")


convidados.insert(1, "Jonas")


del convidados[2]


convidadosRemovidos = convidados.pop()


viajando = "Lucas"

convidados.remove(viajando)


convidados.sort()

print(convidados)
print(len(convidados))

numeros = [3, 2 , 5, 8, 1, 200]
print(min(numeros))
print(max(numeros))


matriz = [
    [5, 12, 3],
    [8, -2, 15],
    [7, 20, 1]
]

print("Matriz: ")

print(matriz[0])
print(matriz[1])
print(matriz[2])

centro = matriz[1][1]
pares = 0


if matriz[0][0] % 2 == 0:
    pares += 1
   
if matriz[0][1] % 2 == 0:
    pares += 1

if matriz[0][2] % 2 == 0:
    pares += 1

if matriz[1][0] % 2 == 0:
    pares += 1

if matriz[1][1] % 2 == 0:
    pares += 1

if matriz[1][2] % 2 == 0:
    pares += 1

if matriz[2][0] % 2 == 0:
    pares += 1

if matriz[2][1] % 2 == 0:
    pares += 1

if matriz[2][2] % 2 == 0:
    pares += 1

print("Quantidade de números pares: ", pares)

if centro < 0:
    print("É negativo!")
else:
    print("Não é negativo!")
