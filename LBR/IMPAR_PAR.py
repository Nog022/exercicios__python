# T <- 1
t = 1

# N <- Ler a quantidade de partidas
n = int(input())

# Enquanto houver casos de teste (ou seja, N != 0) faça
while n != 0:
    # NomePar <- Ler nome do primeiro jogador (escolhe par por definição)
    nome_par = input()
    # NomeImpar <- Ler nome do segundo jogador (escolhe ímpar por definição)
    nome_impar = input()

    # Mostrar "Teste T"
    print('Teste', t)
    # --> print('Teste %d' % t)
    # --> print('Teste {}'.format(t))
    # --> print(f'Teste {t}')

    # Para cada uma das N partidas faça
    for _ in range(n):
        # A, B <- Ler quantidade de dedos da partida atual
        linha = input()
        palavras = linha.split()
        a = int(palavras[0])
        b = int(palavras[1])
        # --> a, b = map(int, input().split())

        # S <- A + B
        s = a + b

        # Se S for par então
        if s % 2 == 0:
            # Mostrar NomePar
            print(nome_par)
        # Se não
        else:
            # Mostra NomeImpar
            print(nome_impar)

    # Mostrar linha e branco
    print()

    # T <- T + 1
    t += 1
    # N <- Ler a quantidade de partidas
    n = int(input())