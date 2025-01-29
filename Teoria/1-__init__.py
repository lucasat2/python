# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))


# O SELF É PARA REFERENCIAR ALGUM OBJETO QUE SERÁ SENDO CRIADO

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

# INSTANCIAMENTO
p1 = Pessoa('Luiz', 'Otávio')
p2 = Pessoa('Maria', 'Joana')

# CHAMANDO OS ATRIBUTOS
print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)