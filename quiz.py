def quiz():
    perguntas = {
        "Qual é a capital da França?": "paris",
        "Quem escreveu 'Dom Quixote'?": "miguel de cervantes",
        "Qual é o maior planeta do sistema solar?": "júpiter",
    }

    pontuacao = 0

    for pergunta, resposta in perguntas.items():
        resposta_usuario = input(pergunta + " ").lower()
        if resposta_usuario == resposta:
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Errado! A resposta correta é {resposta}.")

    print(f"Sua pontuação final é {pontuacao} de {len(perguntas)}.")


quiz()
