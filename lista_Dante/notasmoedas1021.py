#Funções

def calcularMoedas(moedas,dinheiro):
    print('MOEDAS:')
    for moeda in moedas:
        quantida_de_moedas = int(dinheiro / moeda)

        print('{} moeda(s) de R$ {:.2f}'.format(quantida_de_moedas,moeda))
        
        dinheiro -= quantida_de_moedas * moeda 

def calcularNotas(notas,dinheiro):
    print('NOTAS:')
    for nota in notas:
        quantida_de_notas = int(round(dinheiro,2) / nota)

        print('{} nota(s) de R$ {:.2f}'.format(quantida_de_notas,nota))

        dinheiro -= quantida_de_notas * nota 

    calcularMoedas(moedas,dinheiro)


#Principal
dinheiro = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

calcularNotas(notas,dinheiro)