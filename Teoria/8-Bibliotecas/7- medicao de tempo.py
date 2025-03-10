# Medição de Tempo

# Implemente duas formas diferentes de gerar uma lista de números de 1 a 1000000. Use o timeit para comparar o desempenho entre:

# List comprehension
# Loop for tradicional com append numa lista

import timeit

def usando_list_comprehension():
    return [i for i in range(1_000_000)]

def usando_loop_tradicional():
    lista = []
    for i in range(1_000_000):
        lista.append(i)
    return lista

# Medindo o tempo de execução
tempo_list_comprehension = timeit.timeit(usando_list_comprehension, number=10)
tempo_loop_tradicional = timeit.timeit(usando_loop_tradicional, number=10)

print(f"List Comprehension: {tempo_list_comprehension:.5f} segundos")
print(f"Loop Tradicional: {tempo_loop_tradicional:.5f} segundos")

"""
Este código mede o tempo de execução de cada abordagem usando timeit.timeit(), executando cada função 10 vezes para obter uma média mais precisa
"""