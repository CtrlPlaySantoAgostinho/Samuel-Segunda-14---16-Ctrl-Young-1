saldo = 0

while True:

    print("---Caixa Eletronico---")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha sua opção: ")

    if opcao == "1":
        print("Seu saldo é: ", saldo)

    elif opcao == "2":
        deposito = float(input("Digite o valor do depósito: "))

        if deposito > 0:
            saldo+=deposito
            print("Deposito realizado!!! Seu saldo atual é: ", saldo)
        else:
            print("Valor invalido! O deposito deve ser positivo.")

    elif opcao == "3":
        saque = float(input("Digite o valor do saque: "))

        if saque <= 0:
            print("Valor invalido! O saque deve ser positivo.")
        elif saque > saldo:
            print("Saldo Insuficiente")
        else:
            saldo-=saque
            print("Saque realizado!!! Seu saldo atual é: ", saldo)
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção Invalida")

