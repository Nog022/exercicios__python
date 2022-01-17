def calulando_numero_perfeito(num,var):
    somando_divisores = 0

    for i in range(1,num):
        if num % i == 0:
            somando_divisores += i
        
    if num == somando_divisores:
        print('{} eh perfeito'.format(num))
    
    else:
        print('{} nao eh perfeito'.format(num))

#Programa principal
num_teste = int(input())

for i in range(num_teste):
    num = int(input())
    var = num
    var = int(var)
    calulando_numero_perfeito(num,var)