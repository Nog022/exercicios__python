def menor_indice(lista):
    menor = lista[a]
    ind = a
    for i in range(a,b):
        if menor > lista[i+1]:
            menor = lista[i+1]
            ind = i+1
    print(ind)
    

n = int(input())
lista= []

for _ in range(n):
    lista.append(int(input()))

indices = int(input())

for _ in range(indices):
    a = int(input())
    b = int(input())
    menor_indice(lista)