j,r = map(int, input().split()) #jogadores #rodadas

l = j*r #pontos de vitorias

pontos = list(map(int, input().split()))

lista = [0]*j

for i in range(len(pontos)):
    lista[i%j] += pontos[i]

vencedor = 0

for i in range(len(lista)):
    j_atual = lista[i]
    p_vencedor = lista[vencedor]

    if j_atual >= p_vencedor:
        vencedor = i

print(vencedor +1)



