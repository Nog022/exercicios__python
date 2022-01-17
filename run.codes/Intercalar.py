N = int(input())
M = int(input())

s = N + M

A = []
B = []


for i in range(N):
    P = int(input())
    A.append(P)
#print(A)

for j in range(M):
    Q = int(input())
    B.append(Q)
#print(B)
C = []

for k in range(0,N):
    C.append(A[k])
    C.append((B[k]))
for l in range(N,M):
    C.append(B[l])

print(C)


