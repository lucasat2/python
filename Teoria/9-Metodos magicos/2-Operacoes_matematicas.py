class Saldo:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro):
        return Saldo(self.valor + outro.valor)

    def __sub__(self, outro):
        return Saldo(self.valor - outro.valor)


s1 = Saldo(500)  # Saldo de 500
s2 = Saldo(200)  # Saldo de 200
s3 = s1 + s2

print(f"Tipo de s3 é: {type(s3)}")  # Saída esperada: <class  '__main__.Saldo'> (o __main__ pode variar)
print(f"Soma dos saldos: {s3.valor}")  # Saída esperada: 700 
s4 = s1 - s2
print(f"Tipo de s4 é: {type(s4)}")  # Saída esperada: <class '__main__.Saldo'> (o __main__ pode variar)
print(f"Subtração dos saldos: {s4.valor}")  # Saída esperada: 300
