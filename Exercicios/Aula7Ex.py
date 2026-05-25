# Uma função para calcular a média
# Uma função para verificar a situação
# Uma função principal para exibir o resultado

def calcular_media(notas):
    return sum(notas) / len(notas)

# Média ≥ 7 → Aprovado
# Média ≥ 5 → Recuperação
# Média < 5 → Reprovado

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def mostrar_boletim(nome, notas):
    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    print(f"Aluno: {nome}")
    print(f"Média: {media}")
    print(f"Situação: {situacao}")


mostrar_boletim("Zacarias", [10,8,3])


