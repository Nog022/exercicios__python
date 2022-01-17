n = int(input())

ant,atual = 0,1
crescente = True

while n > 0:
    if ant <= atual:
       ant = atual
       atual = int(input())
       n = n - 1


    else:
        atual = int(input())
        n = n - 1
        crescente = False


if crescente == True:
   print('sim')

else:
    print('não')






