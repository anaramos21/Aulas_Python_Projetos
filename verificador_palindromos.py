def verificar_palindromo():
    frase = input("Digite uma palavra ou frase: ").replace(" ", "").lower()
    if frase == frase[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")

verificar_palindromo()
