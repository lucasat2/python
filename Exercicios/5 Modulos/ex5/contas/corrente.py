class ContaCorrente:
    def __init__(self, numero, limite):
        self.numero = numero
        self.saldo = 0.0
        self.limite = limite

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            raise ValueError("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and self.saldo + self.limite >= valor:
            self.saldo -= valor
        else:
            raise ValueError("Saldo insuficiente ou valor inválido.")

    def descricao(self):
        return f"Conta Corrente {self.numero}: Saldo = R$ {self.saldo:.2f}, Limite = R$ {self.limite:.2f}"