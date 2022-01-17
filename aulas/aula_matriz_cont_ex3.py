n = int(input())

A = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input()))
    A.append(linha)

B = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input()))
    B.append(linha)

identidade = True
for i in range(n):              #pecorre a linha  
    for j in range(n):           #coluna na matriz I
        pe = 0                    #produro escalar
        for k in range(n):         #pela coluna j e B
            pe += A[i][k]*B[k][j] 

        if i==j and pe != 1:         #elemnto da diagonal
            identidade = False
            break
        if i!=j and pe!=1:             #elemnto fora da diagonal
            identidade = False
            break

if identidade:
    print('Matrizes são inversas')
else:
    print('matrizes não são inversas')