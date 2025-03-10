"""
Cálculo do Valor Total por Venda:
Crie uma list comprehension para gerar uma nova lista, onde cada elemento seja o valor total de cada venda (preço unitário * quantidade).
"""

# ARMAZENANDO EM UMA LISTA DE TUPLAS OS DADOS DE VENDAS
dados_vendas = [
    ("Camiseta", 25.00, 3), 
    ("Calça Jeans", 80.00, 1), 
    ("Tênis", 150.00, 2), 
    ("Meias", 10.00, 5), 
    ("Casaco", 120.00, 1)
    
]

"""
Produtos com Preço Acima de X:
Crie uma list comprehension para gerar uma nova lista contendo apenas os nomes dos produtos cujo preço unitário seja maior que um valor X (fornecido pelo usuário).
"""
totais_vendas = [(nome, preco_unitario * quantidade, quantidade) for nome, preco_unitario, quantidade in dados_vendas]

for nome, total, quantidade in totais_vendas:
    print(f"Item: {nome}, Total: R${total:.2f}")
    print("\n")

"""

Vendas com Quantidade Superior a Y:
Crie uma list comprehension para gerar uma nova lista contendo tuplas (produto, valor_total) apenas das vendas cuja quantidade seja superior a um valor Y (fornecido pelo usuário).
"""

valor_usuario = float(input("Digite um valor para filtrar os produtos com preço acima: "))

vendas_maiores = [(nome, total) for nome, total, quantidade in totais_vendas if total > valor_usuario]

print("\n")
print(f"Produtos com preço acima de R${valor_usuario:.2f}:")
for nome, total in vendas_maiores:
    print(f"Item: {nome}, Total: R${total:.2f}")
    print("\n")

"""
Vendas com Quantidade Superior a Y:
Crie uma list comprehension para gerar uma nova lista contendo tuplas (produto, valor_total) apenas das vendas cuja quantidade seja superior a um valor Y (fornecido pelo usuário).
 """

quantidade_usuario = int(input("Digite um valor para filtrar as vendas com quantidade superior: "))

vendas_quantidade = [(nome, total, quantidade) for nome, total, quantidade in totais_vendas if quantidade > quantidade_usuario]

print("\n")
print(f"Vendas com quantidade superior a {quantidade_usuario}:")
for nome, total, quantidade in vendas_quantidade:
    print(f"Item: {nome}, Total: R${total:.2f}, Quantidade: {quantidade}")
    print("\n")