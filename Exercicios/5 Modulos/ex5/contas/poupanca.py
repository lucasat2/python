class ContaPoupanca:
    def __init__(self, numero, taxa_juros):
        self.numero = numero
        self.saldo = 0.0
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            raise ValueError("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
        else:
            raise ValueError("Saldo insuficiente ou valor inválido.")

    def aplicar_juros(self):
        self.saldo += self.saldo * self.taxa_juros / 100

    def descricao(self):
        return f"Conta Poupança {self.numero}: Saldo = R$ {self.saldo:.2f}, Taxa de Juros = {self.taxa_juros}%"