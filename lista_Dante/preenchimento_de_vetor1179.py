def arrayLotadoimpar(numerosImpares):
    for i in range(5):
        print('impar[{}] = {}'.format(i,numeroPares))

def arrayLotadoPar(numeroPares):
    for i in range(5):
        print('par[{}] = {}'.format(i,numeroPares))

testes = 15

numeroPares = []
numerosImpares = []
numP = len(numeroPares)
numI = len(numerosImpares)


for i in range(testes):
    num = int(input())

    if numP == 5:
        arrayLotadoPar(numeroPares)

    if numI == 5:
        arrayLotadoimpar(numerosImpares)


    if num % 2 == 0:
        numeroPares.append(num)

    else:
        numerosImpares.append(num)