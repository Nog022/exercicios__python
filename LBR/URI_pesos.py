n = int(input())

v_f = False
lista = list(map(int, input().split()))
i = 0

while i < n:
    if i == 0:
        if lista[i - 0]  <=8:
            v_f = True
            i += 1
        else:
            v_f = False
            i += 1
            break
    else:
        if (lista[i] - lista[i-1]) <= 8:
            v_f = True
            i += 1
        else:
            v_f = False
            i += 1
            break

if v_f == True:
    print('S')

else:
    print('N')