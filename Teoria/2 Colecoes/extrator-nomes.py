
definir_nome = input("Digite o nome completo: ")

palavras = definir_nome.split()

ultimo_sobrenome = palavras[-1].capitalize()


iniciais = []
for palavra in palavras[: -1]:
  iniciais.append(palavra[0].upper() + '.') #Coloca no array a primeira letra da palavra e a transforma em letra maiuscula com um pontinho no final.

# Junta o último sobrenome com as iniciais, separando por vírgula
nome_formatado = ultimo_sobrenome + ", " + " ".join(iniciais)

print(nome_formatado)

"""
Ler um nome completo, com vários nomes e sobrenomes. 

Extrair o último sobrenome (verificar o separador espaço entre os nomes). 

Colocar as iniciais dos nomes anteriores, exceto o último sobrenome, em que cada inicial em maiúscula e acompanhada com um ponto. 

Lembrar de colocar uma vírgula entre o último sobrenome e as iniciais. 

Isto é a formação de nomes de autores em citações no padrão ABNT.

Exemplo: Paulo Marcotti 🡺 Marcotti, P.

Exemplo: Joaquim DA SILVA xavier 🡺 Xavier, J. D. S.

Exemplo: Pedro Alvares CABRAL 🡺 Cabral, P. A.

Sugestão: comece com split() para quebrar em palavras

"""