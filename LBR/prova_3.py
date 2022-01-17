inicio = int(input())

for i in range(inicio):
    t = 0

    c = int(input())

    inicio = []
    for i2 in range(c):
        L = list(input().split())

        if L[0] == 'EXEC':
            L[0] = inicio[int(L[1])-1]

        if L[0] == 'ESQ':
            t -= 1

        if L[0] == 'DIR':
            t += 1
        inicio.extend(L)
    print(t)
