def ate_o_um(h0):
    lista= [h0]
    cont = 0
    while 1 != lista[cont]:

        if lista[cont] % 2 == 0:
                v = (1/2)*lista[cont]
                v = int(v)
                lista.append(v)
                cont += 1
                if 1 == lista[cont]:
                    maior_numero(lista)
        else:
                v_2 = 3*lista[cont] + 1
                v_2 = int(v_2)
                lista.append(v_2)
                cont += 1
                if 1 == lista[cont]:
                    maior_numero(lista)


def maior_numero(lista):
    maior = lista[0]
    for i in range(len(lista)-1):
        if maior < lista[i+1]:
            maior = lista[i+1]
    print(maior)

h0 = int(input())
ate_o_um(h0)
            
        
