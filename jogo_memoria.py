'''No início de cada nível, observe a sequência de números que será mostrada.
Digite os números na mesma ordem em que foram mostrados assim que for solicitado.
Avance de nível à medida que acerta a sequência completa.
O jogo termina quando o jogador erra a sequência.'''

import random
import time

def gerar_sequencia(tamanho):
    return [random.randint(1, 9) for _ in range(tamanho)]

def mostrar_sequencia(sequencia):
    for elemento in sequencia:
        print(elemento, end=' ')
        time.sleep(1)  # Intervalo de 1 segundo entre cada número
        print('\b' * len(str(elemento)), end='', flush=True)  # Apaga o número após mostrar

def obter_palpite(tamanho):
    try:
        return [int(input(f"Digite o {i+1}º número da sequência: ")) for i in range(tamanho)]
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")
        return []

def verificar_sequencias(seq_original, seq_usuario):
    return seq_original == seq_usuario

def jogo_memoria():
    nivel = 1
    while True:
        print(f"\nNível {nivel}:")
        sequencia_original = gerar_sequencia(nivel)
        mostrar_sequencia(sequencia_original)
        palpite_usuario = obter_palpite(nivel)

        if verificar_sequencias(sequencia_original, palpite_usuario):
            print("Correto! Avançando para o próximo nível.")
            nivel += 1
        else:
            print("Incorreto! Fim de jogo.")
            break

jogo_memoria()
