from gerenciamento_de_contatos import*
opcao = 1

while opcao != 4:
    print("Escolha uma opção:\n1-Adicionar contatos\n2-Listar contatos\n3-Remover contatos\n4-Sair")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        contato = input("Digite o contato que deseja adicionar:")
        adicionar_contato(contato)
    elif opcao == 2:
        print("Lista de contatos:")
        listar_agenda()
    elif opcao == 3:
        indice_remover = int(input("Digite o índice do contato que deseja remover: "))
        excluir_contato(indice_remover)
    elif opcao > 4 or opcao < 1:
        print("índice inválido!")
    else:
        print("Finalizando programa")
        
    
