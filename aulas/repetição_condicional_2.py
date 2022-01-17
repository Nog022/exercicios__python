num = 10
contador_pares = 0
continua = True

while continua:
    if num % 2 == 0:
        contador_pares = contador_pares + 1
    num = num + 1
    if (num > 13):
        continua = False
print(contador_pares)