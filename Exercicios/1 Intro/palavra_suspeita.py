# Programa para contar palavras em uma mensagem

# Entrada do usuário
mensagem = input("Digite a mensagem: ")

# Processamento
# Transformar a mensagem em letras minúsculas e separar por palavras
palavras = mensagem.lower().split()

# Contar a frequência de cada palavra
contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

# Ordenar as palavras em ordem alfabética
palavras_ordenadas = sorted(contagem.items())

# Saída
for palavra, quantidade in palavras_ordenadas:
    print(f"{palavra}: {quantidade}")
