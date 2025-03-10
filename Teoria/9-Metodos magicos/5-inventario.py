class Inventario:
    def __init__(self):
        self.itens = {}

    def __setitem__(self, chave, valor):
        self.itens[chave] = valor

    def __getitem__(self, chave):
        return self.itens.get(chave, 0)

    def __delitem__(self, chave):
        if chave in self.itens:
            del self.itens[chave]

    def __iadd__(self, chave_valor):
        chave, valor = chave_valor
        self.itens[chave] = self.itens.get(chave, 0) + valor
        return self

    def __isub__(self, chave_valor):
        chave, valor = chave_valor
        self.itens[chave] = max(self.itens.get(chave, 0) - valor, 0)
        return self

# Criar o inventário
inventario = Inventario()

# Adicionar itens
inventario['maçã'] = 50
inventario['banana'] = 100

# Recuperar a quantidade de um item
print(f"Quantidade de maçãs: {inventario['maçã']}")  # Saída esperada: 50
print(f"Quantidade de bananas: {inventario['banana']}")  # Saída esperada: 100

# Remover um item
del inventario['banana']

# Recuperar a quantidade de um item que não está no inventário
print(f"Quantidade de batatas: {inventario['batata']}")  # Saída esperada: 0
print(f"Quantidade de bananas: {inventario['banana']}")  # Saída esperada: 0

# Incrementar a quantidade de um item
inventario['maçã'] += 5

print(f"Quantidade de maçãs após incremento: {inventario['maçã']}")  # Saída esperada: 55

# Decrementar a quantidade de um item
inventario['maçã'] -= 10

print(f"Quantidade de maçãs após decremento: {inventario['maçã']}")  # Saída esperada: 45
