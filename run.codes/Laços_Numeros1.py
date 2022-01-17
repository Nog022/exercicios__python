n = int(input())
if n != 0:

    outros = int(input())
    soma = (outros)
    produto= (outros)
    menor = (outros)
    maior= (outros)

    for i in range(1,n):
        outros = int(input())
        soma += outros
        produto *= outros

        if outros > maior:
            maior = outros

        if outros < menor:
            menor = outros

    media = (soma / n)
    print('%.2f'%media)
    print(soma)
    print(produto)
    print(menor)
    print(maior)

