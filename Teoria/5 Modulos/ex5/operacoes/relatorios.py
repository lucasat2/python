def listar_clientes(clientes):
    for cliente in clientes:
        print(cliente.descricao())
        if cliente.contas:
            for conta in cliente.contas:
                print(f"  - {conta.descricao()}")
        else:
            print("  Nenhuma conta associada.")

def listar_contas(contas):
    for conta in contas:
        print(conta.descricao())
