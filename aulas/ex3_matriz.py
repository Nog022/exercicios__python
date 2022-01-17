n = int(input())


matriz = []

for i in range(n): 
    linha = []
    for j in range(n):
        linha.append(int(input()))
    matriz.append(linha)
print(matriz)


#Principal
soma_p = 0
for i in range(n):
    soma_p += matriz[i][i]

#Secundaria
soma_s = 0
for i in range(n):
    soma_s += matriz[i][n-1-i]
print(soma_p,soma_s)   