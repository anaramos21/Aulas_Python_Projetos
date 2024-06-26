def calcular_imc():
    while True:
        try:
            peso = float(input("Digite seu peso em kg: "))
            altura = float(input("Digite sua altura em metros: "))
            break
        except ValueError:
            print("Por favor, digite valores numéricos válidos.")

    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Classificação: Peso normal")
    elif 25 <= imc < 29.9:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obesidade")


calcular_imc()
