'''Use as teclas "w" (para cima), "s" (para baixo), "a" (para esquerda) e "d" (para direita) para mover o jogador.
O objetivo é mover o jogador "P" até a saída "S" do labirinto.
O jogo termina quando o jogador encontra a saída.'''
def imprimir_labirinto(labirinto, jogador_pos):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if (i, j) == jogador_pos:
                print("P", end=" ")
            else:
                print(labirinto[i][j], end=" ")
        print()


def movimentar_jogador(pos, direcao, labirinto):
    x, y = pos
    if direcao == 'w' and x > 0 and labirinto[x - 1][y] != '#':
        return (x - 1, y)
    elif direcao == 's' and x < len(labirinto) - 1 and labirinto[x + 1][y] != '#':
        return (x + 1, y)
    elif direcao == 'a' and y > 0 and labirinto[x][y - 1] != '#':
        return (x, y - 1)
    elif direcao == 'd' and y < len(labirinto[0]) - 1 and labirinto[x][y + 1] != '#':
        return (x, y + 1)
    return pos


def jogo_labirinto():
    labirinto = [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', 'S', '#']
    ]

    jogador_pos = (1, 1)
    saida_pos = (6, 5)

    print("Bem-vindo ao jogo de Labirinto!")
    print("Use 'w' para cima, 's' para baixo, 'a' para esquerda, 'd' para direita.")
    print("Encontre a saída marcada com 'S'.")

    while True:
        imprimir_labirinto(labirinto, jogador_pos)
        movimento = input("Faça seu movimento (w/s/a/d): ").lower()
        if movimento in ['w', 'a', 's', 'd']:
            jogador_pos = movimentar_jogador(jogador_pos, movimento, labirinto)
            if jogador_pos == saida_pos:
                print("Parabéns! Você encontrou a saída!")
                break
        else:
            print("Movimento inválido! Use apenas 'w', 'a', 's', 'd'.")


jogo_labirinto()
