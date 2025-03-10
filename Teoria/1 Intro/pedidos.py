# Sistema de pedidos de restaurante

# Dicionário fixo do cardápio
cardapio = {"batata frita": 5.50, "hambúrguer": 10.00, "suco": 4.00, "refrigerante": 3.50}

# Entrada do usuário
pedidos = input("Digite os pedidos, separados por vírgulas: ")

# Processamento

# split(","): Divide a string de pedidos em uma lista, com base nas vírgulas.
# strip(): Remove espaços extras antes ou depois de cada pedido.
# lower(): Converte os pedidos para letras minúsculas, para facilitar a comparação com o cardápio.

pedidos_lista = [pedido.strip().lower() for pedido in pedidos.split(",")]
total = 0.0
pratos_invalidos = []

for pedido in pedidos_lista:
    if pedido in cardapio:
        total += cardapio[pedido]
    else:
        pratos_invalidos.append(pedido)
        
#         Para cada item na lista de pedidos, verifica se está no cardápio:
# Se estiver, o preço é somado ao total.
# Se não estiver, é adicionado à lista de pratos_invalidos.

# Saída
print(f"Total: {total:.2f}")
if pratos_invalidos:
    print(f"Pratos inválidos: {', '.join(pratos_invalidos)}")
    
# Exibe o total formatado com duas casas decimais.
# Se houver pratos inválidos, eles são exibidos como uma lista separada por vírgulas.
