# Inicializar o MENOR_FINAL esforço com um valor absurdamente grande
#   e INDICE_FINAL com um valor qualquer
menor_final = 1000 * 1000  # N máximo vezes Hi máximo, ou usar sys.maxsize
indice_final = -1

# Para cada uma das trilhas faça
n = int(input())
for t in range(n):
    # Ler as alturas da trilha atual
    linha = input()
    palavras = linha.split()
    m = int(palavras[0])
    h = []
    for i in range(1, m+1):
        altura = int(palavras[i])
        h.append(altura)

    # --> m, *h = map(int, input().split())

    # Calcular MENOR_ATUAL como o esforço da trilha atual, onde
    #   ele é o menor esforço entre a ida e a volta
    esforco_ida = 0
    for i in range(0, m-1):
        desnivel = h[i+1] - h[i]
        if desnivel > 0:
            esforco_ida += desnivel

    esforco_volta = 0
    for i in range(m-1, 0, -1):
        desnivel = h[i-1] - h[i]
        if desnivel > 0:
            esforco_volta += desnivel

    if esforco_ida < esforco_volta:
        menor_atual = esforco_ida
    else:
        menor_atual = esforco_volta

    # Se MENOR_ATUAL for menor que MENOR_FINAL então
    if menor_atual < menor_final:
        # Substituo o MENOR_FINAL pelo MENOR_ATUAL, e o INDICE_FINAL por T
        menor_final = menor_atual
        indice_final = t

# Mostrar a trilha de menor esforço
print(indice_final + 1)