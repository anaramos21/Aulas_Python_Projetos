import random


def pedra_papel_tesoura():
    escolhas = ["pedra", "papel", "tesoura"]
    vitorias = {'pedra': 'tesoura', 'papel': 'pedra', 'tesoura': 'papel'}

    while True:
        escolha_usuario = input("Escolha pedra, papel ou tesoura (ou digite 'sair' para sair): ").lower()
        if escolha_usuario == 'sair':
            print("Jogo encerrado.")
            break
        if escolha_usuario not in escolhas:
            print("Escolha inválida! Tente novamente.")
            continue

        escolha_computador = random.choice(escolhas)
        print(f"Computador escolheu: {escolha_computador}")

        if escolha_usuario == escolha_computador:
            print("Empate!")
        elif vitorias[escolha_usuario] == escolha_computador:
            print("Você venceu!")
        else:
            print("Você perdeu!")


pedra_papel_tesoura()
