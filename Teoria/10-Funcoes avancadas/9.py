# Crie um pipeline de geradores para processar uma lista de strings. O pipeline deve consistir de três etapas:

# Uma função geradora converter_maiusculas(strings) que recebe uma sequência de strings e retorna cada string convertida para maiúsculas.
# Uma função geradora filtrar_strings(strings, tamanho_minimo) que recebe uma sequência de strings e um inteiro tamanho_minimo, e retorna apenas as strings que têm um comprimento maior ou igual a tamanho_minimo.
# Uma função geradora limitar_quantidade(strings, quantidade) que recebe uma sequência de strings e um inteiro quantidade, e retorna no máximo quantidade strings da sequência.
# Aplique o pipeline a uma lista de strings de sua escolha, definindo tamanho_minimo como 5 e quantidade como 3.


def converter_maiusculas(strings):
    """Converte cada string da sequência para maiúsculas."""
    for string in strings:
        yield string.upper()

def filtrar_strings(strings, tamanho_minimo):
    """Filtra as strings que têm um comprimento maior ou igual a tamanho_minimo."""
    for string in strings:
        if len(string) >= tamanho_minimo:
            yield string

def limitar_quantidade(strings, quantidade):
    """Retorna no máximo 'quantidade' strings da sequência."""
    contador = 0
    for string in strings:
        if contador < quantidade:
            yield string
            contador += 1
        else:
            break

# Lista de exemplo
lista_strings = ["maçã", "banana", "uva", "abacaxi", "kiwi", "laranja"]

# Aplicação do pipeline
gerador = converter_maiusculas(lista_strings)
gerador = filtrar_strings(gerador, tamanho_minimo=5)
gerador = limitar_quantidade(gerador, quantidade=3)

# Exibição dos resultados
print(list(gerador))
