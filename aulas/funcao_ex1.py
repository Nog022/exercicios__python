def status(nome,media):
    if media > 6:
        print('Aprovado')
    elif media == 4 or media == 5 or media == 6:
        print('Verificação suplemntar')
    else:
        print('Reprovado')


for i in range(5):
    nome = str(input())
    media = float(input())
    status(nome,meida)