def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def quilometros_para_milhas(quilometros):
    return quilometros * 0.621371

def conversor_unidades():
    print("Bem-vindo ao Conversor de Unidades!")
    while True:
        print("\nEscolha a conversão:")
        print("1. Celsius para Fahrenheit")
        print("2. Quilômetros para Milhas")
        print("3. Sair")

        escolha = input("Digite a opção (1/2/3): ")

        if escolha == '3':
            print("Saindo do conversor de unidades. Até mais!")
            break

        if escolha == '1':
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f"{celsius}°C é igual a {fahrenheit}°F")
        elif escolha == '2':
            quilometros = float(input("Digite a distância em quilômetros: "))
            milhas = quilometros_para_milhas(quilometros)
            print(f"{quilometros} km é igual a {milhas} milhas")
        else:
            print("Opção inválida. Tente novamente.")

conversor_unidades()
