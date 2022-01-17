n = int(input())
minhaMatriz = []

for i in range(n):
    linhaDaMatriz = []
    for j in range(n):
        numeroLido = int(input())
        linhaDaMatriz.append(numeroLido)
    minhaMatriz.append(linhaDaMatriz)

matrizMultiplicada = []
for i in range(len(minhaMatriz)):
    linhaMatriz1 = minhaMatriz[i]
    novaLinha = []
    for j in range(len(minhaMatriz)):
        somaDaLinha = 0
        for k in range(len(minhaMatriz[j])):
            n1 = minhaMatriz[i][k]
            n2 = minhaMatriz[k][j]
            somaDaLinha += n1 * n2
        novaLinha.append(somaDaLinha)
    matrizMultiplicada.append(novaLinha)

i, j = 0, 0
matrizTransposta = []
for i in range(len(minhaMatriz)):
    listaAuxiliarTransposta = []
    for j in range(len(minhaMatriz[i])):
        listaAuxiliarTransposta.append(minhaMatriz[j][i])
    matrizTransposta.append(listaAuxiliarTransposta)

matrizSomada = []
for i in range(len(matrizMultiplicada)):
    listaAuxiliarMatrizSomada = []
    for j in range(len(matrizTransposta[i])):
        n1 = matrizMultiplicada[i][j]
        n2 = matrizTransposta[i][j]
        listaAuxiliarMatrizSomada.append(n1 + n2)
    matrizSomada.append(listaAuxiliarMatrizSomada)

print(matrizSomada)