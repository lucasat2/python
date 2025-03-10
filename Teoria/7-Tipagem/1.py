from typing import List

def calcular_desconto(preco: float) -> float:
    return preco * 0.9

def juntar_nomes(nomes: List[str]) -> str:

    return ", ".join(nomes)


if __name__ == "__main__":
    #  calcular_desconto
    preco_original = 100.0
    print(f"Preço original: {preco_original}")
    print(f"Preço com desconto: {calcular_desconto(preco_original)}")

    # juntar_nomes
    lista_nomes = ["Ana", "João", "Maria"]
    print(f"Nomes: {juntar_nomes(lista_nomes)}")
