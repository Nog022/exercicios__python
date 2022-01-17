t = 1
n = int(input())
    
while n != -1:
    total = (1+(2**n))*(1+(2**n))

    print('Teste',t)
    print(total)
    print('')
    t += 1
    n = int(input())