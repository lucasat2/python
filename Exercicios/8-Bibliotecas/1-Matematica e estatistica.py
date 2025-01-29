import random  # Biblioteca para gerar números aleatórios
import statistics  # Biblioteca para cálculos estatísticos
import math  # Biblioteca para cálculos matemáticos avançados

def main():
    # Gerar uma lista de 50 números inteiros aleatórios entre 1 e 100
    numeros = [random.randint(1, 100) for _ in range(50)]
    
    # Calcular a média dos números gerados
    media = statistics.mean(numeros)
    
    # Calcular a mediana dos números gerados
    mediana = statistics.median(numeros)
    
    # Encontrar o maior valor na lista
    maior_valor = max(numeros)
    
    # Encontrar o menor valor na lista
    menor_valor = min(numeros)
    
    # Calcular a raiz quadrada do maior número
    raiz_quadrada_maior = math.sqrt(maior_valor)

    # Exibir os resultados com explicações claras
    print("=== Resultados Estatísticos ===")
    print(f"Números gerados: {numeros}")  # Mostrar a lista de números gerados
    print(f"Média: {media:.2f}")  # Exibir a média com 2 casas decimais
    print(f"Mediana: {mediana}")  # Exibir a mediana
    print(f"Maior valor: {maior_valor}")  # Exibir o maior valor
    print(f"Menor valor: {menor_valor}")  # Exibir o menor valor
    print(f"Raiz quadrada do maior valor ({maior_valor}): {raiz_quadrada_maior:.2f}")  # Exibir a raiz quadrada

if __name__ == "__main__":
    main()  # Chamar a função principal para executar o programa

# A mediana é o valor central em uma lista ordenada de números. 
# Se houver dois números centrais (como em uma lista com quantidade par de elementos), 
# a mediana será a média desses dois números.
