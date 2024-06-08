agenda = []

def adicionar_contato(nome, telefone):
    novo_contato = {'nome': nome, 'telefone': telefone}
    agenda.append(novo_contato)
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos():
    if agenda:
        print("Lista de Contatos:")
        for contato in agenda:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
    else:
        print("Não há contatos na agenda.")

def remover_contato(nome):
    for contato in agenda:
        if contato['nome'] == nome:
            agenda.remove(contato)
            print(f"Contato {nome} removido com sucesso!")
            return
    print(f"Contato {nome} não encontrado na agenda.")


def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Remover Contato")
    print("4. Sair")

opcao = True
while opcao:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(nome, telefone)
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        nome = input("Digite o nome do contato que deseja remover: ")
        remover_contato(nome)
    elif opcao == "4":
        print("Encerrando o programa...")
        opcao = False
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")