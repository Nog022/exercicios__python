import math
#Opções da calculadora
print('Digite 1 para soma')
print('Digite 2 para subtração')
print('Digite 3 para multiplicação')
print('Digite 4 para divisão')
print('Digite 5 para raiz quadrada')
print('Digite 6 para porcentagem')
print()

#Funções
def calcular_soma(primeiro_numero,segundo_numero):
    
    return primeiro_numero + segundo_numero

def calcular_sub(primeiro_numero,segundo_numero):

    return primeiro_numero - segundo_numero  


def calcular_multiplicacao(primeiro_numero,segundo_numero):

    return primeiro_numero * segundo_numero


def calcular_divisao(primeiro_numero,segundo_numero):

    return primeiro_numero // segundo_numero


def calcular_raiz_quadrada(numero_da_opcao):
    if numero_da_opcao == 5:

        numero = int(input('Digite um numero: '))
        
        return math.sqrt(numero)

def inteiro_para_decimal(porcentagem):
    return porcentagem / 100


def calcular_porcentagem(numero_da_opcao):
    if numero_da_opcao == 6:
        print('Digite um numero:')

        numero = int(input())

        print('Digite a porcentagem')

        porcentagem = int(input())

        decimal = inteiro_para_decimal(porcentagem)
    

        return print('Esse é o resultado: {}%'.format(numero * decimal))        


def calculadora():

    if numero_da_opcao == 1:

        primeiro_numero = int(input('Digite um número: '))

        segundo_numero = int(input('Digite outro: '))

        soma = calcular_soma(primeiro_numero,segundo_numero)

        print('Esse é o resultado: {}'.format(soma))

    elif numero_da_opcao == 2:

        primeiro_numero = int(input('Digite um número: '))

        segundo_numero = int(input('Digite outro: '))

        subtracao = calcular_sub(primeiro_numero,segundo_numero)

        print('Esse é o resultado: {}'.format(subtracao))

    elif numero_da_opcao == 3:

        primeiro_numero = int(input('Digite um número: '))

        segundo_numero = int(input('Digite outro: '))

        multiplicao = calcular_multiplicacao(primeiro_numero,segundo_numero)

        print('Esse é o resultado: {}'.format(multiplicao))

    elif numero_da_opcao == 4:

        primeiro_numero = int(input('Digite um número: '))

        segundo_numero = int(input('Digite outro: '))

        divisao = calcular_divisao(primeiro_numero,segundo_numero)

        print('Esse é o resultado: {}'.format(divisao))
    
    elif numero_da_opcao == 5:

        resultado_da_raiz = calcular_raiz_quadrada(numero_da_opcao)
        
        print('Esse é o resultado: {}'.format(resultado_da_raiz))

    elif numero_da_opcao == 6:

        calcular_porcentagem(numero_da_opcao)


#Programa Principal
numero_da_opcao = int(input())

calculadora()
