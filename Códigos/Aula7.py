#Calculadora

def soma(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a-b
    elif op == "*":
        return a * b
    elif op == "/":
        return a/b
    else:
        return "Operação Inválida"
    
#Maior número

def maior(a,b):
    if a >= b:
        return a
    else:
        return b
    

def velocidade(tempo, distancia):
    print(distancia/tempo)


velocidade(4, 1000)
