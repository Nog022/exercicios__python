N = []
for i in range(20):
    N.append(int(input()))
    aux = 0
    aux = N[i]
    N[i] = N[i-1]
    N[i-1] = N[i]
    print('N[{}] = {}'.format(i, N[i]))