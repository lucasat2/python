class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso

    def calcular_frete(self):
        return self.peso * 0.1

class Eletronico(Produto):
    def __init__(self, nome, preco, peso, voltagem):
        super().__init__(nome, preco, peso)
        self.voltagem = voltagem

class Livro(Produto):
    def __init__(self, nome, preco, peso, autor):
        super().__init__(nome, preco, peso)
        self.autor = autor

# Exemplo de uso
eletronico = Eletronico("Smartphone", 1500, 0.5, "220V")
livro = Livro("Python Programming", 100, 0.3, "Autor Desconhecido")

print(f"Frete do eletrônico: {eletronico.calcular_frete()}")
print(f"Frete do livro: {livro.calcular_frete()}")