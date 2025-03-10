# Use as funções map() e filter() com funções lambda para processar uma lista de números. Primeiro, use map() para elevar cada número ao quadrado. Em seguida, use filter() para manter apenas os números que são maiores que 10.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_quadrado= list(map(lambda x: x**2, lista_numeros))

numeros_filtrados = list(filter(lambda x: x > 10, numeros_quadrado))

print(numeros_filtrados)