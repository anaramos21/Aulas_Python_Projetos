import random

def escolher_palavra():
    palavras = ['python', 'desenvolvimento', 'jogo', 'programacao', 'algoritmo']
    return random.choice(palavras).upper()

def jogo_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("_ " * len(palavra))

    while tentativas > 0:
        tentativa = input("Digite uma letra: ").upper()

        if tentativa in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_adivinhadas.append(tentativa)

        if tentativa in palavra:
            print("Boa! A letra está na palavra.")
        else:
            tentativas -= 1
            print(f"Errado! Você tem {tentativas} tentativas restantes.")

        palavra_oculta = "".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])
        print(" ".join(palavra_oculta))

        if "_" not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra.")
            break

    if tentativas == 0:
        print(f"Você perdeu! A palavra era {palavra}")

jogo_forca()
