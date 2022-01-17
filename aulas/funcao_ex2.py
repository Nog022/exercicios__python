def linha_nula(matriz):
    nulas = 0
    for i in range(len(matriz)):
        cont = 0
        for j in range(len(matriz)):
            if matriz[i][j] == 0:
                cont += 1
            if cont == n:
                nulas =+ 1
    print(f'Tem {nulas} linhas nulas ')                

n = int(input())

matriz = []
for _ in range(n):
    l = []
    for j in range(n):
        l.append(int(input()))
    matriz.append(l)
linha_nula(matriz)



