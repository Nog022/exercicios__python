madeira_altura = list(map(int, input().split()))

cerca = list(map(int, input().split()))

n_madeira = madeira_altura[0]

altura = madeira_altura[1]

cont = 0

while not all(_ == altura for _ in cerca):
    for x in range(n_madeira):
        if x != n_madeira-1:
            while cerca[x] < altura:
                cerca[x] += 1
                cerca[x + 1] += 1
                cont += 1
            while cerca[x] > altura:
                cerca[x] -= 1
                cerca[x + 1] -= 1
                cont += 1
        else:
            while cerca[x] < altura:
                cerca[x] += 1
                cont += 1
            while cerca[x] < altura:
                cerca[x] += 1
                cont += 1
print(cont)