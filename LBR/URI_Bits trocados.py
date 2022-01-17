t = 1
moedas = int(input())
while moedas != 0 :

    print(f'Teste {t}')
    
    moeda50 = moedas // 50
    resto = moedas % 50
    moeda10 = resto // 10
    resto = resto % 10
    moeda5 = resto // 5
    resto = resto % 5
    
    print("{} {} {} {} ".format(moeda50, moeda10, moeda5, resto))
    
    print()

    t += 1    

    moedas = int(input())