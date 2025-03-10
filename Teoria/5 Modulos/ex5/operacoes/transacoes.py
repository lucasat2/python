def depositar(contas):
    numero = int(input("Digite o número da conta: "))
    conta = next((c for c in contas if c.numero == numero), None)
    if conta:
        valor = obter_input_positivo("Digite o valor do depósito: ")
        conta.depositar(valor)
        print("Depósito realizado com sucesso.")
    else:
        print("Conta não encontrada.")

def sacar(contas):
    numero = int(input("Digite o número da conta: "))
    conta = next((c for c in contas if c.numero == numero), None)
    if conta:
        valor = obter_input_positivo("Digite o valor do saque: ")
        conta.sacar(valor)
        print("Saque realizado com sucesso.")
    else:
        print("Conta não encontrada.")

def aplicar_juros(contas):
    numero = int(input("Digite o número da conta poupança: "))
    conta = next((c for c in contas if c.numero == numero and isinstance(c, ContaPoupanca)), None)
    if conta:
        conta.aplicar_juros()
        print("Juros aplicados com sucesso.")
    else:
        print("Conta poupança não encontrada.")