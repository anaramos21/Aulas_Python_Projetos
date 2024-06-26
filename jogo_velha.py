def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for linha in tabuleiro:
        if all(s == jogador for s in linha):
            return True
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    turno = 0

    print("Bem-vindo ao Jogo da Velha!")
    while True:
        exibir_tabuleiro(tabuleiro)
        jogador = jogadores[turno % 2]
        print(f"Turno do jogador {jogador}")

        while True:
            try:
                linha = int(input("Digite a linha (0, 1, 2): "))
                coluna = int(input("Digite a coluna (0, 1, 2): "))
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador
                    break
                else:
                    print("Posição já ocupada. Tente novamente.")
            except (ValueError, IndexError):
                print("Entrada inválida. Digite números entre 0 e 2.")

        if verificar_vitoria(tabuleiro, jogador):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador} venceu!")
            break

        if all(tabuleiro[linha][coluna] != " " for linha in range(3) for coluna in range(3)):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        turno += 1

jogo_da_velha()
