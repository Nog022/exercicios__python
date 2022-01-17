op = input('Deseja somar (S) ou multiplicar (M)?')
x = int(input('Digite um número:'))
y = int(input('Digite outro:'))

if (op == "S"):
    r = x + y
    print('O resultado da soma é', r)
elif (op == "M"):
    r = x * y
    print('O resultado da multiplicação é', r)
else:
    print('Opção invalida')
