import random


def simulador_dados():
    while True:
        try:
            numero_dados = int(input("Digite o número de dados: "))
            lados_dados = int(input("Digite o número de lados em cada dado: "))
            break
        except ValueError:
            print("Por favor, digite números inteiros válidos.")

    resultados = [random.randint(1, lados_dados) for _ in range(numero_dados)]
    print(f"Resultados dos lançamentos: {resultados}")


simulador_dados()
