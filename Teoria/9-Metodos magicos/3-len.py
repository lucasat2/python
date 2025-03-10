# Criando uma classe que suporta o comando “len()”

# Implemente uma classe chamada Livro que representa um livro com capítulos. A classe deve:

# Armazenar capítulos em uma lista interna privada.

# Retornar o número de capítulos ao usar a função len() na instância da classe (__len__).

class Livro : 
  def __init__(self):
    self.capitulos = []

  def adicionar_capitulo(self, capitulo):
    self.capitulos.append(capitulo)

  def __len__(self):
    return self.capitulos 

livro = Livro()
livro.adicionar_capitulo("Capítulo 1: Introdução")
livro.adicionar_capitulo("Capítulo 2: Desenvolvimento")

print(f"O livro tem {len(livro)} capitulos")  