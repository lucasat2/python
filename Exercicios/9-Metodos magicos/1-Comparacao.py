class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __eq__(self, outro):
        if isinstance(outro, Produto):
            return self.preco == outro.preco
        return False

    def __lt__(self, outro):
        if isinstance(outro, Produto):
            return self.preco < outro.preco
        return False

    def __gt__(self, outro):
        if isinstance(outro, Produto):
            return self.preco > outro.preco
        return False

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

    def __repr__(self):
        return f"Produto(nome={self.nome}, preco={self.preco})"

if __name__ == "__main__":
    
    cafe = Produto("Café", 15.90)
    pao = Produto("Pão", 8.50)
    laptop = Produto("Notebook", 3500.00)
    mouse = Produto("Mouse", 50.00)
    mousepad = Produto("Mousepad", 50.00)
    
    
    print(f"{cafe} > {pao}? {cafe > pao}")  # True (15.90 > 8.50)
    print(f"{mouse} < {laptop}? {mouse < laptop}")  # True (50.00 < 3500.00)
    print(f"{mouse} == {mousepad}? {mouse == mousepad}")  # True (50.00 == 50.00)
    print(f"{pao} != {laptop}? {pao != laptop}") # True (8.50 != 3500.00)

 