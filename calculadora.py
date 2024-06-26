def calculadora():
    print("Bem-vindo à Calculadora!")
    while True:
        print("\nEscolha a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite a opção (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo da calculadora. Até mais!")
            break

        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif escolha == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Tente novamente.")


# se desejo retornar ao menu inicial após a execução chamo novamente a função calculadora()
