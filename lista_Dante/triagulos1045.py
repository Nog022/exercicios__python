#Funções
def ordernando(A,B,C,lista):
    
    
    lista.sort()
    
    A = lista[2]
    B = lista[1]
    C = lista[0]
    return A,B,C
    
    
    


def nao_forma(A,B,C):
    n = 0
    b_c = B + C
    while n == 0:
        if A >= b_c:
            print('NAO FORMA TRIANGULO')
            break
        

def tri_retangulo(A,B,C):
    b_c = (B**2) + (C**2)
    A = A**2
    if A == b_c:
        return print('TRIANGULO RETANGULO')

def tri_obtusangulo(A,B,C):
    b_c = (B**2) + (C**2)
    A = A**2
    if A > b_c:
        return print('TRIANGULO OBTUSANGULO')
        
def tri_acutangulo(A,B,C):
    b_c = (B**2) + (C**2)
    A = A**2
    if A < b_c:
        return print('TRIANGULO ACUTANGULO')

def tri_equilatero(A,B,C):
    if A == B and B == C:
        return print('TRIANGULO EQUILATERO')

def tri_isosceles(A,B,C):
    if A == B and A != C:
        return print('TRIANGULO ISOSCELES')
    
    elif A == C and C != B:
        return print('TRIANGULO ISOSCELES')
    
    elif B == C and B != A:
        return print('TRIANGULO ISOSCELES')


#Programa Principal
A,B,C = map(float,input().split())
lista = [A,B,C]

A,B,C = ordernando(A,B,C,lista)
nao_forma(A,B,C)
tri_retangulo(A,B,C)
tri_obtusangulo(A,B,C)
tri_acutangulo(A,B,C)
tri_equilatero(A,B,C)
tri_isosceles(A,B,C)


#se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
#se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
#se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
#se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
#se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
#se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES