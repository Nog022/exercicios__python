n = int(input())
m = int(input())
p = int(input())

A = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(int(input()))
    A.append(linha)

B = []
for i in range(m):
    linha = []
    for j in range(p):
        linha.append(int(input()))
    B.append(linha)

C = []
for i in range(n):
    C.append([0]*p) 

for i in range(n):  #percorre a linha
    for j in range(p): #coluna da matriz c
        for k in range(m):#pelas coluna j e b
            C[i][j] += A[i][k] * B[k][j]
        

for i in range(n):
    print(C[i])