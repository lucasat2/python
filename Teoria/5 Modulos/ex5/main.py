from operacoes import cadastrar_cliente, criar_conta, depositar, sacar, aplicar_juros, listar_clientes, listar_contas

def main():
    clientes = []
    contas = []

    while True:
        print("\nSistema Bancário")
        print("1. Cadastrar Cliente")
        print("2. Criar Conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Aplicar Juros (Poupança)")
        print("6. Listar Clientes")
        print("7. Listar Contas")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente(clientes)
        elif opcao == "2":
            criar_conta(clientes, contas)
        elif opcao == "3":
            depositar(contas)
        elif opcao == "4":
            sacar(contas)
        elif opcao == "5":
            aplicar_juros(contas)
        elif opcao == "6":
            listar_clientes(clientes)
        elif opcao == "7":
            listar_contas(contas)
        elif opcao == "8":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
