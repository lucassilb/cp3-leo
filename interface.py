tarefas = []


def cadastrar_tarefa(lista, descricao, data_vencimento, status):
    tarefa = {
        "descricao": descricao,
        "data_vencimento": data_vencimento,
        "status": status
    }

    lista.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas(lista):
    if not lista:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n===== LISTA DE TAREFAS =====")

    for i, tarefa in enumerate(lista, start=1):
        print(
            f"{i} - "
            f"Descrição: {tarefa['descricao']} | "
            f"Vencimento: {tarefa['data_vencimento']} | "
            f"Status: {tarefa['status']}"
        )


def atualizar_tarefa(lista, indice, nova_descricao, nova_data, novo_status):
    if 0 <= indice < len(lista):
        lista[indice]["descricao"] = nova_descricao
        lista[indice]["data_vencimento"] = nova_data
        lista[indice]["status"] = novo_status
        print("Tarefa atualizada com sucesso!")
    else:
        print("Índice inválido.")


def excluir_tarefa(lista, indice):
    if 0 <= indice < len(lista):
        lista.pop(indice)
        print("Tarefa excluída com sucesso!")
    else:
        print("Índice inválido.")


def menu():
    while True:
        print("\n===== MENU DE TAREFAS =====")
        print("1 - Cadastrar tarefa")
        print("2 - Listar tarefas")
        print("3 - Atualizar tarefa")
        print("4 - Excluir tarefa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            data = input("Digite a data de vencimento: ")
            status = input("Digite o status da tarefa: ")

            cadastrar_tarefa(tarefas, descricao, data, status)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            listar_tarefas(tarefas)

            if tarefas:
                numero = int(input("Digite o número da tarefa que deseja atualizar: "))
                indice = numero - 1

                nova_descricao = input("Nova descrição: ")
                nova_data = input("Nova data de vencimento: ")
                novo_status = input("Novo status: ")

                atualizar_tarefa(
                    tarefas,
                    indice,
                    nova_descricao,
                    nova_data,
                    novo_status
                )

        elif opcao == "4":
            listar_tarefas(tarefas)

            if tarefas:
                numero = int(input("Digite o número da tarefa que deseja excluir: "))
                indice = numero - 1

                excluir_tarefa(tarefas, indice)

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


def main():
    menu()


if __name__ == "__main__":
    main()