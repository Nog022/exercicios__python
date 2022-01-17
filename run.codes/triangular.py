n_inteiro = int(input())

triangular = False

for x in range (1,n_inteiro//2 ):
    propriedade = x * (x+1) * (x+2)

    if propriedade == n_inteiro:
        triangular = True
        print(x)
        print(x+1)
        print(x+2)

if triangular == False:
 print('não')