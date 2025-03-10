from tarefas import Tarefa
from gerenciador import GerenciadorTarefas

def exibir_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Listar tarefas")
    print("4. Excluir tarefa")
    print("5. Sair")

def main():
    gerenciador = GerenciadorTarefas()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            gerenciador.adicionar_tarefa(descricao)
        elif opcao == "2":
            gerenciador.listar_tarefas()
            try:
                indice = int(input("Digite o índice da tarefa a ser marcada como concluída: "))
                gerenciador.marcar_tarefa_como_concluida(indice)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "3":
            gerenciador.listar_tarefas()
        elif opcao == "4":
            gerenciador.listar_tarefas()
            try:
                indice = int(input("Digite o índice da tarefa a ser excluída: "))
                gerenciador.excluir_tarefa(indice)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "5":
            gerenciador.salvar_tarefas()
            print("Tarefas salvas. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
