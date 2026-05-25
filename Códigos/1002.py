A = float(input())
B = float(input())
C = float(input())

if A < B:
    A, B = B, A
if A < C:
    A, C = C, A
if B < C:
    B,C = C,B


if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A*A == B*B + C*C:
        print("TRIANGULO RETANGULO")
    elif A*A > B*B + C*C:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if A == B and B == C:
        print("TRIANGULO EQUILATERO")
    elif A==B or A==C or B==C:
        print("TRIANGULO ISOCELES")