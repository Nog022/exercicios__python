n = int(input())
multi = 5
adicao = 1
soma = 0

for x in range(1,51):
    if(x % 2 == 0):
        soma += (multi * n)
        multi += 8
    else:
        soma += (adicao + n)
        adicao += 8

print(soma)