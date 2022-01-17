N = int(input())
for _ in range(N):
    somatorio = 0
    lista = []
    for k in range(5):
        k = int(input())
        lista.append(k)
       
    for _ in range(5):
        for i in range(4):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                somatorio += 1
    print(somatorio)            


                


        