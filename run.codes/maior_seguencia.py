def decrescente(lista):
    cont = 1
    maior_seguencia = []
    for i in range(n-1):
        if lista[i] > lista[i+1]:
            cont += 1
            if i == n-2:
                maior_seguencia.append(cont)
        if lista[i] < lista[i+1]:
            maior_seguencia.append(cont)
            cont = 1
        
    maior_da_lista(maior_seguencia)


def maior_da_lista(maior_seguencia):
    maior_num = 0 
    for j in range(len(maior_seguencia)):
        if maior_num < maior_seguencia[j]:
            maior_num = maior_seguencia[j]
    print(maior_num)



n = int(input())
lista = []

for _ in range(n):
    lista.append(int(input()))

decrescente(lista)