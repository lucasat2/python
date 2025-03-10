"""
Você trabalha para uma empresa de logística e precisa criar um programa em Python para gerenciar o controle de estoque de produtos. O programa deve ser capaz de lidar com diferentes armazéns e os produtos armazenados neles.

O desafio consiste em desenvolver um sistema utilizando frozensets para realizar o controle de estoque, permitindo as seguintes funcionalidades:

Armazenamento de Produtos por Armazém:

Crie um programa que permita ao usuário inserir informações sobre os produtos (somente o código do produto basta) presentes em diferentes armazéns. Cada armazém pode ter um conjunto de produtos únicos representados por frozensets, onde os produtos não podem ser alterados após a criação do conjunto.

Consulta de Produtos por Armazém:

Implemente a funcionalidade que permita ao usuário consultar quais produtos estão presentes em um determinado armazém, fornecendo o conjunto de produtos por meio de um frozenset.

Permita que o usuário adicione novos produtos a um determinado armazém. Utilizando frozensets, garanta que a imutabilidade dos conjuntos seja mantida após a adição de novos itens.

Além disso, permita a remoção de produtos de um armazém, mantendo a integridade do conjunto utilizando frozensets.
"""

estoque = {}

while True:
    print("\nMenu:")
    print("1. Adicionar produtos a um armazém")
    print("2. Consultar produtos de um armazém")
    print("3. Remover produtos de um armazém")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome_armazem = input("Digite o nome do armazém: ")
        produtos = input("Digite os códigos dos produtos separados por espaço: ").split()
        if nome_armazem in estoque:
            estoque[nome_armazem] = estoque[nome_armazem].union(frozenset(produtos))
        else:
            estoque[nome_armazem] = frozenset(produtos)
    elif opcao == '2':
        nome_armazem = input("Digite o nome do armazém: ")
        produtos = estoque.get(nome_armazem, frozenset())
        print(f"Produtos no armazém {nome_armazem}: {produtos}")
    elif opcao == '3':
        nome_armazem = input("Digite o nome do armazém: ")
        produtos = input("Digite os códigos dos produtos a serem removidos separados por espaço: ").split()
        if nome_armazem in estoque:
            estoque[nome_armazem] = estoque[nome_armazem].difference(frozenset(produtos))
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")