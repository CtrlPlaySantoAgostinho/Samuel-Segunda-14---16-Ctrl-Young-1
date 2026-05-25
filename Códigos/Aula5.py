numeros = [1,2,3,4,5]

for qualquercoisa in numeros:
    print(qualquercoisa)


for numero in range(1,11):
    print(numero)


for letra in "Samuel":
    print(letra)


for numero in range(1, 1001):
    if numero % 2 == 0:
        print(numero)

i = 10

while i < 100:
    print(i)
    i = i + 1

#break - parar um loop
#continue - ir para o proximo loop
#pass - não faz nada

soma = 0

x = 0

while x < 1000:
    x+=1

    if x % 3 == 0:
        print(x)
        soma += x
    else:
        if x % 5 == 0:
            pass
        else:
            print("buscando...")
            continue
    if soma > 300:
        print(soma)
        break
