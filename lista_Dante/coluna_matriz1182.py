#matriz[12][12]
def calcularMedia(matriz,numero_da_coluna):
    media = 0
    for i in range(12):
        media += matriz[i][numero_da_coluna]
    
    print('{:.1f}'.format(media/12))

def calcularSoma(matriz,numero_da_coluna):
    soma = 0
    for i in range(12):
        soma += matriz[i][numero_da_coluna]
    
    print('{:.1f}'.format(soma))


def somaMedia(soma_ou_media,matriz,numero_da_coluna):
    if soma_ou_media == 'S':
        calcularSoma(matriz,numero_da_coluna)
    
    if soma_ou_media == 'M':
        calcularMedia(matriz,numero_da_coluna)


#Principal
matriz = []

numero_da_coluna = int(input())
soma_ou_media = input()


for i in range(12):
    linha = []

    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

somaMedia(soma_ou_media,matriz,numero_da_coluna)