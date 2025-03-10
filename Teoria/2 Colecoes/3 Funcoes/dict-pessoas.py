# Crie uma função chamada criar_dict_pessoa que recebe nome e idade como argumentos obrigatórios e um número variável de informações adicionais como kwargs. A função deve retornar um dicionário com todos os dados.


def criar_dict_pessoa(nome, idade, **kwargs): ##kwargs é um dicionário

  pessoa = {
    'nome': nome, 
    'idade': idade #cria um dicionário com nome e idade
  } 

  pessoa.update(kwargs) #atualiza o dicionário pessoa com os valores de kwargs
  return pessoa


pessoa2 = criar_dict_pessoa("Lucas", 30, cidade="São Paulo", profissao="Engenheiro")

print(pessoa2)  # Saída: {'nome': 'Lucas', 'idade': 30, 'cidade': 'São Paulo', 'profissao': 'Engenheiro'}

print()

pessoa1 = criar_dict_pessoa("Ana", 25, cidade="Rio de Janeiro")
print(pessoa1)  # Saída: {'nome': 'Ana', 'idade': 25, 'cidade': 'Rio de Janeiro'}