agenda_contatos = []
def adicionar_contato(contato):
    agenda_contatos.append(contato)
    return agenda_contatos


def listar_agenda():
    contador = 1
    for contato in agenda_contatos:
        print(contador, "-", contato)
        contador =+ 1


def excluir_contato(indice_remover):
    listar_agenda()
    if indice_remover-1 == agenda_contatos[indice_remover]:
        agenda_contatos.remove[indice_remover]
        return "Contato removido com sucesso!"
    else:
        return "Índice inválido ou contato não cadastrado"
