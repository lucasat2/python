# Utilize a função sorted() com uma função lambda para ordenar uma lista de tuplas. Cada tupla contém o nome de um produto e seu preço. A lista deve ser ordenada em ordem decrescente de preço.

produtos = [('produto1', 10), ('produto2', 5), ('produto3', 15), ('produto4', 20)]

                                       #Coleta o indice 1 que é o preço
produtos_ordenados = sorted(produtos, key=lambda x: x[1], reverse=True)

print(produtos_ordenados)