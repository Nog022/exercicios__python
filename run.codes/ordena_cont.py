n = int(input())

m = int(input())


Q = n*m
lista = []

for i in range(Q):

    lista.append(int(input()))



Q = len(lista)


for i in range(Q):

    for j in range(i+1,Q):

        if lista[i] < lista[j]:
            t = lista[i]
            lista[i] = lista[j]
            lista[j] = t

final = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(lista[i+j*n])
    final.append(linha)

print(final)


            