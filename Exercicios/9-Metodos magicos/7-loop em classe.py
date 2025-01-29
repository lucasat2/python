"""
Criando uma classe que suporta um loop for

Implemente uma classe chamada Contador que representa uma sequência de números de um valor inicial a um valor final (como se fosse um range). A classe deve implementar os métodos __iter__ e __next__ para permitir iteração.

"""

class Contador:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        self.atual = inicio - 1  # Para iniciar corretamente no __next__

    def __iter__(self):
        return self  # A classe é seu próprio iterador

    def __next__(self):
        if self.atual < self.fim:
            self.atual += 1
            return self.atual
        else:
            raise StopIteration  # Fim da iteração

# Exemplo de uso
contador = Contador(1, 5)

for numero in contador:
    print(numero)


    """
    Resumo da linha 12
    essa linha de código prepara o iterador para começar a partir do valor inicial desejado quando o método __next__ for chamado pela primeira vez. Isso é uma prática comum ao implementar iteradores personalizados em Python, garantindo que a sequência de valores gerada pelo iterador comece no ponto correto.
    """