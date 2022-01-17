#Principal
numero_testes = int(input())

lista = []

for i in range(numero_testes):
    num = int(input())
    lista.append(num)

for i in range(numero_testes):
    vezes_aparecidas = 1
    for j in range(numero_testes+2):
        if lista[i] == lista[j+1]:
            vezes_aparecidas += 1
    
    print('{} aparece {} vez(es)'.format(lista[i], vezes_aparecidas))

        
        