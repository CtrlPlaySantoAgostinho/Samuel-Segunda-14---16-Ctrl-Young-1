# “O programa deve:

# pedir dois números,
# fazer uma divisão,
# tratar erro caso o usuário digite errado,
# e impedir divisão por zero.”





# Exercício: Caixa eletrônico com tratamento de erros

# Crie um programa que simule um caixa eletrônico com as opções:

# Consultar saldo
# Sacar
# Depositar
# Sair
# Regras do programa
# O saldo inicial deve ser 1000.
# O usuário deve escolher uma opção por meio de um menu.
# Se o usuário digitar algo inválido, o programa deve mostrar uma mensagem de erro e pedir novamente.
# Para sacar:
# o valor deve ser um número inteiro ou real válido
# não pode ser menor ou igual a zero
# não pode ser maior que o saldo disponível
# Para depositar:
# o valor deve ser válido
# não pode ser menor ou igual a zero
# O programa deve continuar rodando até o usuário escolher sair.

# No final, usar finally para mostrar uma mensagem de encerramento.
# O que o aluno deve usar
# while True
# try
# except
# else
# finally
# input()
# if, elif, else


saldo = 1000

while True:

    print("---Caixa Eletronico---")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    try:
        opcao = int(input("Escolha sua opção: "))

        if opcao == 1:
            print("Seu saldo é: ", saldo)

        elif opcao == 2:
            deposito = float(input("Digite o valor do depósito: "))

            if deposito > 0:
                saldo+=deposito
                print("Deposito realizado!!! Seu saldo atual é: ", saldo)
            else:
                print("Valor invalido! O deposito deve ser positivo.")

        elif opcao == 3:
            saque = float(input("Digite o valor do saque: "))

            if saque <= 0:
                print("Valor invalido! O saque deve ser positivo.")
            elif saque > saldo:
                print("Saldo Insuficiente")
            else:
                saldo-=saque
                print("Saque realizado!!! Seu saldo atual é: ", saldo)
        elif opcao == 4:
            print("Saindo do sistema...")
            break
        else:
            print("Opção Invalida")

    except:
        print("Entrada inválida. Digite apenas números.")

    finally:
        print("Obrigado por usar o caixa eletrônico")

