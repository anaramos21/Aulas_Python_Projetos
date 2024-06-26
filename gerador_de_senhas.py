import random
import string

def gerar_senha(tamanho=12, maiusculas=True, minusculas=True, numeros=True, especiais=True):
    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Nenhum conjunto de caracteres foi selecionado.")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho = int(input("Digite o tamanho da senha: "))
print("A senha gerada é:", gerar_senha(tamanho))
