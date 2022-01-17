def calcularFibonacci(num,anterior,proximo,var):
    
    
    if num == 0:
        return print("Fib(0) = 0")
    
    if num == 1:
        return print("Fib(1) = 1")

    for i in range(num-1):
        proximo += anterior
        anterior -= proximo 
    
    return print('Fib({}) = {}'.format(num,proximo))
        


#Principal
numero_testes = int(input())

anterior = 0
proximo = 1

var = 0


for i in range(numero_testes):
    num = int(input())
    calcularFibonacci(num,anterior,proximo,var)
