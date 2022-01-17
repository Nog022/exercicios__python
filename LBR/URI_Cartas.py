lista = list(map(int, input().split()))


if lista[0] < lista[1] and  lista[1] < lista[2] and lista[2] < lista[3] and lista[3] < lista[4]:                
    print('C')

elif lista[0] > lista[1] and  lista[1] > lista[2] and lista[2] > lista[3] and lista[3] > lista[4]:
    print('D')

else:
    print('N')
