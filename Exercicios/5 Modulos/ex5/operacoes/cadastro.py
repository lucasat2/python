from ..util import validar_cpf, obter_input_positivo
from ..contas import ContaCorrente, ContaPoupanca

def cadastrar_cliente(clientes):
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    if validar_cpf(cpf):
        cliente = Cliente(nome, cpf)
        clientes.append(cliente)
        print("Cliente cadastrado com sucesso.")
    else:
        print("CPF inválido.")

def criar_conta(clientes, contas):
    cpf = input("Digite o CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    if cliente:
        tipo_conta = input("Digite o tipo de conta (1 - Corrente, 2 - Poupança): ")
        numero = obter_input_positivo("Digite o número da conta: ")
        if tipo_conta == "1":
            limite = obter_input_positivo("Digite o limite da conta corrente: ")
            conta = ContaCorrente(numero, limite)
        elif tipo_conta == "2":
            taxa_juros = obter_input_positivo("Digite a taxa de juros da conta poupança: ")
            conta = ContaPoupanca(numero, taxa_juros)
        else:
            print("Tipo de conta inválido.")
            return
        cliente.adicionar_conta(conta)
        contas.append(conta)
        print("Conta criada com sucesso.")
    else:
        print("Cliente não encontrado.")