R = 1
while R == 1:

    a = int(input())


    n_pnultimo = 1
    n_ultimo = 2
    s = 0

    if a == 1:
        print(1)
    else:
        print(1)
        print(2)

    for i in range(2,a):
        s = n_pnultimo * n_ultimo +1
        n_pnultimo = n_ultimo
        n_ultimo = s
        print(s)

    R = int(input())


