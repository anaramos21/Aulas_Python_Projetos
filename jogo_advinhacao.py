import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while True:
        tentativa = int(input("Digite seu palpite: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif tentativa > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você adivinhou o número secreto em {tentativas} tentativas.")
            break

jogo_adivinhacao()
