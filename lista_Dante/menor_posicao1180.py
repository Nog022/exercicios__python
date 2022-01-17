def passandoParaInt(x,num_testes):
    for i in range(num_testes):
        x[i] = int(x[i])

num_testes = int(input())

vetor = []

x = input().split()
passandoParaInt(x,num_testes)
menor_valor = x[0]
posicao = 0

for i in range(num_testes):
    #menor número
    if x[i] < menor_valor:
        menor_valor  = x[i]
        posicao = i

print('Menor valor: {}'.format(menor_valor))
print('Posicao: {}'.format(posicao))

