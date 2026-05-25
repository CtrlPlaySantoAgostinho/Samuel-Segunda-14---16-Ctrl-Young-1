class Aluno:
    def __init__(self, nome, nota1, nota2, faltas):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.faltas = faltas

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    
    def situacap(self):
        media = self.calcular_media()

        if self.faltas > 5:
            return "Reprovado por Faltas"
        elif media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
        
    
    
