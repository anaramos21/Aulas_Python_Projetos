def exibir_contatos(contatos):
    if not contatos:
        print("Nenhum contato na agenda.")
    else:
        for nome, telefone in contatos.items():
            print(f"Nome: {nome}, Telefone: {telefone}")

def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contatos[nome] = telefone
    print(f"Contato {nome} adicionado com sucesso.")

def editar_contato(contatos):
    nome = input("Digite o nome do contato a ser editado: ")
    if nome in contatos:
        telefone = input("Digite o novo telefone do contato: ")
        contatos[nome] = telefone
        print(f"Contato {nome} atualizado com sucesso.")
    else:
        print("Contato não encontrado.")

def agenda_contatos():
    contatos = {}

    print("Bem-vindo à Agenda de Contatos!")
    while True:
        print("\nEscolha a operação:")
        print("1. Exibir contatos")
        print("2. Adicionar contato")
        print("3. Editar contato")
        print("4. Sair")

        escolha = input("Digite a opção (1/2/3/4): ")

        if escolha == '4':
            print("Saindo da agenda de contatos. Até mais!")
            break

        if escolha == '1':
            exibir_contatos(contatos)
        elif escolha == '2':
            adicionar_contato(contatos)
        elif escolha == '3':
            editar_contato(contatos)
        else:
            print("Opção inválida. Tente novamente.")

agenda_contatos()
