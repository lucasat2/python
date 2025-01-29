# Crie uma classe Produto com anotações de tipo para seus atributos (nome: str, preco: float, quantidade: int) e métodos. Inclua um método que calcula o valor total do produto..

class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self) -> float:
        return self.preco * self.quantidade

    def __str__(self) -> str:

        return f"Produto(Nome:{self.nome}, Preço:{self.preco:.2f}, Quantidade:{self.quantidade})"


if __name__ == "__main__":
    produto = Produto("Caderno", 12.50, 10)
    print(produto)
    print(f"Valor total: R${produto.calcular_valor_total():.2f}")
