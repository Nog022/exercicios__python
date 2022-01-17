moedas = int(input())

moeda100 = moedas // 100
resto = moedas % 100

moeda50 = resto // 50
resto = resto % 50

moeda25 = resto // 25
resto = resto % 25

moeda1 = resto // 1

if (moeda100 == 0):
    pass
else:
    print('{}  de 1r'.format(moeda100))

if (moeda50 == 0):
    pass
else:
    print('{}  de 50c'.format(moeda50))

if (moeda25 == 0):
    pass
else:
    print('{}  de 25c'.format(moeda25))

if (moeda1 == 0):
    pass
else:
    print('{}  de 1c'.format(moeda1))