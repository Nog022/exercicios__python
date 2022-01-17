n = int(input())
v_f = False

R = n//2
cont = R
matriz = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input()))
    matriz.append(l)

if n % 2 == 1:
    matriz_impar = 0
    n_impar = 0
    impar = 0
    cont = R
    for i in range(R):
        for j in range(R):
            matriz_impar += matriz[i][j+1] #parte de cima 
            matriz_impar += matriz[i-1][j+1]                #parte de baixo
            cont -= 1
            n_impar += 2
            if cont ==0:
                impar = matriz_impar/n_impar
                print('%.2f'%impar)
                break

else:
    matriz_par = 0
    n_par = 0
    par = 0
    cont = R
    for i in range(R):
        for j in range(R):
            matriz_par += matriz[i][j+1]
            matriz_par += matriz[i-1][j+1]
            cont -= 1
            n_par += 2 
            if cont == 0:
                par = matriz_par/n_par
                v_f = True
                print('%.2f'%par)
                break





