# Programa 1: Criar e salvar a lista de livros
import json

# Lista de dicionários com informações sobre os livros
livros = [
    {"título": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954},
    {"título": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "ano": 1997},
    {"título": "1984", "autor": "George Orwell", "ano": 1949}
]

# Serializa a lista e salva no arquivo "livro.json"
with open("livro.json", "w", encoding="utf-8") as arquivo:
    json.dump(livros, arquivo, ensure_ascii=False, indent=4)

print("Arquivo 'livro.json' criado com sucesso!")