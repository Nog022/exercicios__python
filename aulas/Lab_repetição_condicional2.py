n = int(input())
numero = 2
primo = True

while numero < n:
    if (n % numero == 0):
        primo = False
    numero = numero + 1

if (primo):
    print(' é primo')
else:
    print('não é primo')


