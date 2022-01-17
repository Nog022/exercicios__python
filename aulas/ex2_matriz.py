n = int(input())
m = int(input())

matriz = []

for i in range(n): #linha
    linha = []
    for j in range(m):
        linha.append(int(input('['+ str(i)+ ',' + str(j) + '[:')))
    matriz.append(linha) 
print(matriz) 

max_soma = 0
linha_max = 0

for i in range(n):
    soma = 0
    for j in range(m):
        soma += matriz[i][j]
    print('linha',i,'tem soma',soma)

    if soma > max_soma or (i==0):
        max_soma = soma
        linha_max = i
print('linha=',linha_max,'soma=',max_soma)