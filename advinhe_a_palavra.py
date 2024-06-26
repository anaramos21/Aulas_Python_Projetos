import random


def embaralhar_palavra(palavra):
    palavra = list(palavra)
    random.shuffle(palavra)
    return ''.join(palavra)


def adivinhe_a_palavra():
    palavras = ["python", "desenvolvimento", "jogo", "programacao", "algoritmo"]
    palavra_secreta = random.choice(palavras)
    palavra_embaralhada = embaralhar_palavra(palavra_secreta)

    print("Bem-vindo ao jogo Adivinhe a Palavra!")
    print(f"A palavra embaralhada é: {palavra_embaralhada}")

    tentativa = input("Qual é a palavra original? ")

    if tentativa == palavra_secreta:
        print("Parabéns! Você adivinhou a palavra.")
    else:
        print(f"Você errou! A palavra correta era {palavra_secreta}.")


adivinhe_a_palavra()
