n = int(input()) #linha
m = int(input()) #coluna

matriz = []
for _ in range(n):
    linha = []
    for i in range(m):
        x = int(input())
        linha.append(x)
    matriz.append(linha)


maior = matriz[0][0]
for k in range(n):
    for j in range(m):
        if maior < matriz[k][j]:
            maior = matriz[k][j]



matriz_final = []
for k in range(n):
    linha_final = []
    for j in range(m):
        elem = matriz[k][j] - maior
        linha_final.append(elem)
    matriz_final.append(linha_final)
print(matriz_final) 