# For - Peça para mostrar a tabuada do 5 (até 5 x 10).
# While - Repetir até digitar "sair"


for numero in range(1,51):
    if numero % 5 == 0:
        print(numero)

for numero in range(1,11):
    print(numero * 5)

palavra = ""

while palavra != "sair":
    palavra = input("Digite uma palavra: ")


#break - parar um loop

