N = int(input())
par = []
impar = []

for k in range(N):
    k = int(input())
    if k % 2 == 0:
        par.append(k)
    else:
        impar.append(k)

for _ in range(len(par)):
    for i in range(len(par)-1):
        if par[i] > par[i+1]:
            par[i], par[i+1] = par[i+1], par[i]

for _ in range(len(impar)):
    for j in range(len(impar)-1):
        if impar[j] < impar[j+1]:
            impar[j], impar[j+1] = impar[j+1], impar[j]

total = par + impar            
print(total)

