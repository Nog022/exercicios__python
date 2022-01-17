n = int(input())
m = int(input())

matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(int(input()))
    matriz.append(linha)

#cada linha 
for k in range(n):
    #ordenar linha por bolha
    for i in range(m):
        for j in range(m-1):
            if matriz[k][j] > matriz[k][j+1]:
                t = matriz[k][j]
                matriz[k][j] = matriz[k][j+1]
                matriz[k][j+1] = t
            
for i in range(n):
    print(matriz[i])