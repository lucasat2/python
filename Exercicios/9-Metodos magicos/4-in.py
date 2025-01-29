"""
Criando uma classe suporta o comando “in”

Implemente uma classe chamada Biblioteca que representa um acervo de livros. A classe deve permitir:

Adicionar livros ao acervo.

Verificar se um livro está na biblioteca usando a palavra-chave in (__contains__).
"""

class Biblioteca:
    def __init__(self):
        self.livros = set() #Cria um conjunto para armazenar os livros.(nao permite duplicatas)

    def adicionar_livro(self, livro): #Adicionar livros ao acervo.
        self.livros.add(livro) #adiciona o livro ao conjunto livros

    def __contains__(self, livro):  #Verificar se um livro está na biblioteca usando in(__contains__).
        return livro in self.livros

# Exemplo de uso:
biblioteca = Biblioteca()
biblioteca.adicionar_livro("O Pequeno Príncipe")
biblioteca.adicionar_livro("1984")

print("O Pequeno Príncipe" in biblioteca)
print("Dom Quixote" in biblioteca)         
