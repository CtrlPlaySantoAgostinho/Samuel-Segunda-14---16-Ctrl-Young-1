def cadastro():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))

    print("Cadastro realizado!")
    print("Nome: ", nome)
    print("Idade: ", idade)
    print("Altura: ", altura)

    if idade < 0:
        print("Idade Invalida")

    elif idade < 18:
        print("Menor de idade")

    else:
        print("Maior de idade")


    if altura < 0.0 or altura >= 3.0:
        print("Altura Invalida")

    if idade >= 12 and altura >= 1.40:
        print(f"{nome} Pode andar no brinquedo")
    else:
        print(F"{nome}Não pode andar no brinquedo")
