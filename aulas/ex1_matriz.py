n = int(input())
m = int(input())

matriz = []

for i in range(n): #linha
    linha = []
    for j in range(m): #coluna
        linha.append(int(input('['+ str(i)+ ',' + str(j) + '[:')))
    matriz.append(linha)
print(matriz)

for i in range(n):
    soma = 0
    for j in range(m):
        soma += matriz[i][j]
    print('linha',i,'tem soma',soma)    
