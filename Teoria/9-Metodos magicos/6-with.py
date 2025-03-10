"""

Criando uma classe que suporta o comando “with”

Implemente uma classe chamada ArquivoTemporario que cria e exclui um arquivo temporário automaticamente. A classe deve:

Criar o arquivo no método __enter__.

Excluir o arquivo no método __exit__.

Exemplo de uso:

with ArquivoTemporario("exemplo.txt") as arquivo:
    arquivo.write("Conteúdo temporário")

# O arquivo "exemplo.txt" é excluído automaticamente após o bloco `with`.

"""

import os

class ArquivoTemporario:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def __enter__(self):
        self.arquivo = open(self.nome_arquivo, 'w')
        return self.arquivo

    def __exit__(self, tipo, valor, traceback):
        self.arquivo.close()
        os.remove(self.nome_arquivo)


with ArquivoTemporario("exemplo.txt") as arquivo:
    arquivo.write("Conteúdo temporário")


