# # diasDaSemanaTupla = ("Segunda", "Segunda", "Terça", "Quarta", "Quinta", "Sexta","Sabado","Domingo")

# # #Tupla é

# # diasDaSemanaSet = set()

# # diasDaSemanaSet.add(1)

# # diasDaSemanaSet.add(1)

# # diasDaSemanaSet.add(1)

# # diasDaSemanaSet.add(2)

# # print(diasDaSemanaSet)

# # #Set inicia vazio e não aceita repetições

# # #Boolean
# # a = True
# # b = False
# # c = None

# # print(a,b,c)

# dicionario = {}

# dicionario["Tree"] = "Arvore"

# dicionario["Dog"] = "Cachorro"

# dicionario["Cat"] = "Gato"



# print(dicionario.keys())

# print(dicionario.values())


# print("Ola\n\tBernardo")



dicionario = {
    "dog": "cachorro",
    "cat": "gato",
    "tree": "árvore",
    "car": "carro",
    "house": "casa"
}

palavra = input("Digite uma palavra em inglês: ").lower()

if palavra in dicionario:
        print("Tradução: ", dicionario[palavra])
else:
        print("Palavra não encontrada")

for chave in dicionario:
    print(chave)


