def tribonacci(lista):    
    if n >= 3:  
        for i in range(n-3):
            calculo = lista[i] + lista[i+1] + lista[i+2]
            lista.append(calculo)
        print(lista)

    if n == 2:
        print('[1,1]')
    if n == 1:
        print('[1]')

n = int(input())

lista = [1,1,2]
tribonacci(lista)
