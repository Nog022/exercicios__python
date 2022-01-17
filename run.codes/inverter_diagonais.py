n = int(input())

matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        x = int(input())
        linha.append(x)
    matriz.append(linha)

for i in range(n):
    t = matriz[i][i]  
    matriz[i][i] = matriz[i][n-1-i]
    matriz[i][n-1-i] = t

for i in range(n // 2):
    matriz[0][i], matriz[0][n - 1 - i] = matriz[0][n - 1 - i], matriz[0][i]

print(matriz)
