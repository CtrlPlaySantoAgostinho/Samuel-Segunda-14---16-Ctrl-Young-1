def nota():
    while True:
        nota = float(input("Digite a nota: "))
        nome = input("Digite o nome do aluno: ")

        if nota < 0 or nota > 10:
            print("Nota invalida: ",nota)
        elif nota < 5:
            print(nome," esta reprovado na materia")
        elif nota > 5 and nota < 6.9:
            print(nome,"esta de recuperação na materia")
        else:
            print(nome," esta aprovado na materia")