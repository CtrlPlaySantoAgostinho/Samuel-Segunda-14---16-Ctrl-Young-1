# r = read - lendo oque esta nele
# w - write - apaga tudo e escreve por cima
# a - append - adiciona ao arquivo
# r+ - ler e escrever

with open("frutas.txt", "r") as arquivo:
    print("Frutas no arquivo:")
    print(arquivo.read())

fruta = input("Digite uma fruta: ")

with open("frutas.txt", "a") as arquivo:
    arquivo.write(fruta + "\n")

print("Fruta adicionada com sucesso!")

with open("frutas.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print("Quantidade de linhas:", len(linhas))

with open("frutas.txt", "r") as arquivo:
    print("Lista de frutas:")
    for linha in arquivo:
        print(linha.strip())

# 🟢 Exercício 1 – Criar e ler (Fácil)

# Crie um arquivo frutas.txt e escreva 3 frutas nele com codigo.
# Depois mostre tudo na tela.

# 🟡 Exercício 2 – Adicionar (Fácil/Médio)

# Peça uma fruta ao usuário e adicione no arquivo sem apagar as anteriores.

# 🟡 Exercício 3 – Contar linhas (Médio)

# Mostre quantas linhas existem no arquivo.

# 🔥 DESAFIO

# Crie um sistema de tarefas:

# Usuário digita tarefa
# Salva no arquivo
# Mostra todas ao final