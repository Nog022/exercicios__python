N = int(input())

lista = []

for j in range(N):
    contem = False
    x = int(input())
    for k in range(len(lista)):
        if x == lista[k]:
            contem = True
    if not contem:
        lista.append(x)
            
    
for _ in range(len(lista)):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
print(lista)        