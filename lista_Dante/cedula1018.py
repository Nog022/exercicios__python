dinheiro_inicial = int(input())

nota100 = dinheiro_inicial // 100
resto = dinheiro_inicial % 100

nota50 = resto // 50
resto = resto % 50

nota20 = resto // 20
resto = resto % 20

nota10 = resto // 10
resto = resto % 10

nota5 = resto // 5
resto = resto % 5

nota2 = resto // 2
resto = resto % 2

nota1 = resto // 1


print(dinheiro_inicial)

print('{} nota(s) de R$ 100,00'.format(nota100))


print('{} nota(s) de R$ 50,00'.format(nota50))


print('{} nota(s) de R$ 20,00'.format(nota20))


print('{} nota(s) de R$ 10,00'.format(nota10))


print('{} nota(s) de R$ 5,00'.format(nota5))


print('{} nota(s) de R$ 2,00'.format(nota2))


print('{} nota(s) de R$ 1,00'.format(nota1))
