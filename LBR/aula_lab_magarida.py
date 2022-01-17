# Ler lista original
lista = list(map(float, input().split()))
n = len(lista)

# Calcular a lista acumulada
lista_acumulada = [None] * n
lista_acumulada[0] = lista[0]
for i in range(1, n):
    lista_acumulada[i] = lista_acumulada[i-1] + lista[i]

# Calcular o somatório no intervalo [i, j]
i, j = map(int, input().split())

if i != 0:
    soma = lista_acumulada[j] - lista_acumulada[i-1]
else:
    soma = lista_acumulada[j]

soma = (lista_acumulada[j] - lista_acumulada[i-1]) if i != 0 else lista_acumulada[j]