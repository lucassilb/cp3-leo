def cadastrar_tarefa(lista, descricao, data_vencimento, status):
    tarefa = {
        "descricao": descricao,
        "data_vencimento": data_vencimento,
        "status": status
    }

    lista.append(tarefa)


def listar_tarefas(lista):
    if not lista:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n===== LISTA DE TAREFAS =====")

    for i, tarefa in enumerate(lista, start=1):
        
            f"{i} - "
            f"Descrição: {tarefa['descricao']} | "
            f"Vencimento: {tarefa['data_vencimento']} | "
            f"Status: {tarefa['status']}"
        )


def atualizar_tarefa(
    lista
    indice,
    nova_descricao,
    nova_data
    novo_status
):
    if 0 <= indice < len(lista):

        lista[indice]["descricao"] = nova_descricao
        lista[indice]["data_vencimento"] = nova_data
        lista[indice]["status"] = novo_status

    else:
        print("Tarefa não encontrada.")


def remover_tarefa(lista, indice):
    if 0 <= indice < len(lista):

        lista.pop(indice)

    else:
        print("Tarefa não encontrada.")