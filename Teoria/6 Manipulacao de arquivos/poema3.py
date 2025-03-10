# Programa 3: Escreva um programa que leia o arquivo “poema.txt” linha a linha e conte quantas palavras existem no arquivo (assuma que cada palavra é separada por um espaço das demais).

def contar_palavras(arquivo):  
  with open(arquivo, 'r', encoding='utf-8') as file:  # Abre o arquivo no modo de leitura com codificação UTF-8
    conteudo = file.read()  # Lê todo o conteúdo do arquivo e armazena na variável 'conteudo'
    palavras = conteudo.split()  # Divide o conteúdo em palavras, usando espaços como delimitadores, e armazena na lista 'palavras'
    return len(palavras)  # Retorna o número de palavras na lista 'palavras'

if __name__ == "__main__":  
  nome_arquivo = 'poema.txt'  # Define o nome do arquivo a ser lido
  total_palavras = contar_palavras(nome_arquivo)  # Chama a função contar_palavras e armazena o resultado em 'total_palavras'
  print(f"O total de palavras no arquivo '{nome_arquivo}' é: {total_palavras}") 