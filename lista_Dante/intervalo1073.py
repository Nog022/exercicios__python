#intervalo entre 10 a 20
numero_de_testes = int(input())

dentro = 0
fora = 0

for i in range(numero_de_testes):
    N = int(input())
    if N < 10:
        fora += 1
    elif N > 20:
        fora += 1
    else:
        dentro += 1

print('{} in'.format(dentro))
print('{} out'.format(fora))
