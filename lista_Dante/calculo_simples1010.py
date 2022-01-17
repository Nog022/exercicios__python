#Funções
def seta_valores(lista_valores):
    codigo = int(lista_valores[0])
    peca = int(lista_valores[1])
    valor = float(lista_valores[2])
    
    return codigo, peca, valor


def calcular_total(lista_valores):
    codigo, peca, valor = seta_valores(lista_valores)
    return peca * valor

#Principal
total_geral = 0
for i in range(2):
    split = input().split()
    total_peca = calcular_total(split)
    total_geral += total_peca

print(f"VALOR A PAGAR: R$ {total_geral:.2f}")




#split_1 = input().split()
#codigo1 = int(split_1[0])
#peca1 = int(split_1[1])
#valor1 = float(split_1[2])

#split_2 = input().split()
#codigo2 = int(split_2[0])
#peca2 = int(split_2[1])
#valor2 = float(split_2[2])


##calculo = (valor1 * peca1) + (valor2 * peca2)

#print("VALOR A PAGAR: R$ %.2f" % (calculo))



