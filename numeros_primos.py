def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gerar_primos():
    while True:
        try:
            inicio = int(input("Digite o início do intervalo: "))
            fim = int(input("Digite o fim do intervalo: "))
            break
        except ValueError:
            print("Por favor, digite números inteiros válidos.")

    primos = [num for num in range(inicio, fim + 1) if eh_primo(num)]
    print(f"Números primos no intervalo [{inicio}, {fim}]: {primos}")


gerar_primos()
