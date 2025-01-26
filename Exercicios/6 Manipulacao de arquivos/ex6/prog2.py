# Programa 2: Ler e imprimir a lista de livros
# Lê o arquivo "livro.json" e desserializa para uma lista
def imprimir_livros():
    with open("livro.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

    # Imprime cada livro no formato especificado
    for livro in livros:
        print(f"Título: {livro['título']}, Autor: {livro['autor']}, Ano: {livro['ano']}")

if __name__ == "__main__":
    imprimir_livros()
