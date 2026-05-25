convidados = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
convidados[2] = "Fernanda"
convidados.append("Gabriel")
convidados.insert(1, "Helena")
removido = convidados.pop()


def conferirLista():
    nome = input("Digite um nome para verificar na lista: ")
    if nome in convidados:
        print(nome + " está confirmado na festa!")
    else:
        print(nome + " NÃO está na lista de convidados!")

def tamanhoDaLista():
    if len(convidados) > 5:
        print("A festa terá muitos convidados!")
    else:
        print("A festa será mais reservada.")