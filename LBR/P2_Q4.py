#numero de cartas solicitadas 
n = int(input())
#lista de cartas 
cartas = list(map(int, input().split()))
#maior valor das cartas 
maiorvalor = [1]

total_reset = 1
for i in range(len(cartas)-1):
    if cartas[i] == cartas[i+1]:
        total_reset += 1         
    else:
        total_reset = 1           
    maiorvalor.append(total_reset)
maiorvalor.sort()
print(maiorvalor[n-1])

