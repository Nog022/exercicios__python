N = int(input())

A = []
copia = []
for i in range (1, N+1):
    a = int(input())
    A.append(a)
    copia.append(a)


Y = 1
for x in range(N//2):
    A[x] = A[N-Y]
    A[N-Y] = copia[x]
    Y += 1


B = []


for b in range(0, N):
    if A[b] >= 0:
        fatorial = 1
        for y in range(1, A[b]+1):
            #print(A[b])
            fatorial *= y
        B.append(fatorial)
    else:
        B.append(A[b])


print(B)


