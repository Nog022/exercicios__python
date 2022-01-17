#n <-- ler quantidade de raios

n = int(input())

# Criar o mapa completo da cidade

mapa = [None] * 501
for y in range(501):
    mapa[y] = [False] * 501

# Mito <-- 0, pois por enquanto ele é verdadeiro

mito = 0

# Para cada um dos N raios faça
for t in range(n):
    # X , Y <-- Ler as coordenadas do raio atual
    x,y = map(int, input().split())

    #Verificar se o mito é falso

    if mapa[y][x]:
        # Mito <-- 1, pois foi detectado que o mito é falso
        mito = 1
        # Interrompe a repetição
        break
    # Se não, # colocar o par (X,Y) na lista Raios
    else:
        mapa[y][x] = True

# Mostrar o valor da variavél Mito
print()