n = int(input())

matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        x =  int(input())
        linha.append(x)
    matriz.append(linha)

soma = 0
for i in range(len(matriz)):
  for j in range(i + 1, len(matriz)):
    soma += matriz[i][j]
print(soma)

t = n*n

soma_antes_media = 0
for i in range(n):
    for j in range(n):
        soma_antes_media += matriz[i][j]
media_total = soma_antes_media/t

cont = 0
for i in range(n):
    for j in range(n):
        if matriz[i][j] < media_total:
            cont += 1
print(cont)